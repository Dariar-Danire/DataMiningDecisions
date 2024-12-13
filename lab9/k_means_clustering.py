import random
from collections import defaultdict
from math import sqrt
from dsmltf import squared_distance, distance
from matplotlib import pyplot


def find_best_k(dataset, max_k=8, min_k=2):
    """
    Вычисляет лучшее k для кластеризации методом k средних соседей
    :param dataset: Список исходных точек
    :param max_k: Максимальное k (по умолчанию 8)
    :param min_k: Минимальное k (по умолчанию 2)
    :return: Лучшее k для кластеризации переданного датасета
    """

    # Определяем словарь для суммарных квадративных отклонений для каждого числа кластеров
    errors_for_k = dict()

    # Заполняем errors_for_k
    for k in range(min_k, max_k + 1):
        k_clusters = clustering(dataset, k)
        if k_clusters[0] == 0:
            continue

        errors = 0
        for k_i in range(k):
            # Считаем суммарное квадратичное отклонение для каждого числа кластеров
            errors += sum([squared_distance(point, k_clusters[0][k_i]) for point in k_clusters[1][k_i]])
        sqrt_errors = sqrt(errors)

        # Добавляем нужное отклонение для текущего k
        errors_for_k[k] = sqrt_errors

    # Находим лучшее k с помощью коэфициентов
    all_k = list(errors_for_k.keys())
    max_coefficient = -float('inf')
    best_k = 0
    for i in range(len(all_k)):
        if i == 0 or i == len(all_k) - 1:
            continue

        # Вычисляем коэфициент для текущего k
        curr_coeff = (errors_for_k[all_k[i - 1]] - errors_for_k[all_k[i]]) / abs(errors_for_k[all_k[i]] - errors_for_k[all_k[i + 1]])
        if curr_coeff > max_coefficient:
            max_coefficient = curr_coeff
            best_k = min_k + all_k[i]

    # Строим график
    pyplot.plot(all_k, list(errors_for_k.values()))
    pyplot.title("Квадатичные отклонения для каждого k")
    pyplot.grid()
    pyplot.xlabel("k")
    pyplot.ylabel("Квадратичные отклонения")
    pyplot.show()

    print(f"Лучшее k - {best_k} \n")

    return best_k


def clustering(data, k):
    """
    Кластеизация методом k средних.
    :param data: Матрица с данными, которые нужно кластеризовать (list of lists)
    :param k: Число кластеов (int)
    :return: new_С (dict) - центы кластеов,
             G (dict) - кластеры
    """

    try:
        # Генеиуем случайные центры кластеров
        C = rand_centers(data, k)

        # Распределяем точки по кластерам
        G = group(C, data)

        # Вычисляем новые центры кластеров
        new_C = step_centers(G)

        # До тех пор, пока центры кластеров не перестают смещаться,
        # пересчитываем кластеры и их центры
        while compare(C, new_C):
            C = dict(new_C)
            G = group(C, data)
            new_C = step_centers(G)

        return dict(new_C), dict(G)
    except Exception as e:
        print(f"Error at k = {k}! {e}")
        return 0, 0


def rand_centers(data, k):
    """
    Инициализирует случайные центры кластеров для первой итерации
    :param data: Список точек
    :param k: Количество кластеров
    :return: Словарь случайных центров кластеров
    """
    # Оеделяем словарь для центов кластеов
    centers = defaultdict(list)

    # Определяем шаг для равномерного распределения начальных центров
    offset = int(len(data) / k)
    for i in range(k):
        try:
            # Выбираем случайную точку из датасета как центр i-го кластера
            centers[i] = (data[random.randint(offset * i, offset * (i + 1) - 1)])
        except IndexError:
            print(f'i = {i}, offset = {offset}')

    return centers


def group(C, data):
    """
    Распределяет точки датасета по ближайшим к ним кластерам
    :param C: Словарь центров кластеров
    :param data: Список точек (датасет)
    :return: Словарь с кластерами
    """

    # Определяем словарь для кластеров
    clusters = defaultdict(list)

    for d in data:
        d_inf = float('inf')
        i = 0

        for j in C.keys():
            # Находим ближайший к этой точке центр кластера
            dist = distance(d, C[j])
            if dist < d_inf:
                i = j
                d_inf = dist

        # Записываем точку в соответствующий кластер
        clusters[i].append(d)

    return clusters


def step_centers(G):
    """
    Вычисляет новые центры кластеров как средние точки текущих кластеров
    :param G: Словарь с кластерами
    :return: Словарь новых центров кластеров
    """

    # Определяем словарь для центров кластеров
    new_C = defaultdict(list)

    for k in G.keys():
        n = len(G[k][0])  # Количество координат (признаков) у точки

        # Для каждой координаты
        for i in range(n):
            # Находим i-ю координату центра k-го кластер как
            # среднее значение i-го признака для всех точек в кластере
            new_C[k].append(sum(g[i] for g in G[k]) / len(G[k]))

    return new_C


def compare(C1, C2, m=2):
    """
    Проверяет сдвигаются ли центры кластеров в процессе кластеризации
    :param C1: Предыдущие центры кластеров
    :param C2: Новые центры кластеров
    :param m: до какого знака после запятой округлять
    :return: True - если центр хотя бы одного кластера сдвинулся и False в противном случае
    """

    # Определяем список, который будет содержать результаты вычислений
    check_list = []

    for k in C1.keys():
        # Вычисляем разницу между предыдущими центрами и новыми центрами k-го кластера
        check_list.append(round(sum((c1-c2)**2
                                    for c1, c2 in zip(C1[k], C2[k])), m))

    return any(check_list)
