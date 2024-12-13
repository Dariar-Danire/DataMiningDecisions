
def rising_clustering(data: list, dist, size: float) -> dict:
    """
    Реализация алгоритма восходящей кластеризации
    :param data: Список точек
    :param dist: Функция, с помощью которой меряется расстояние
    :param size: Максимальное расстояние между кластерами.
    :return: Словарь кластеров
    """

    # Каждую точку данных делаем кластерами
    clusters = {}
    for i, d in enumerate(data):
        clusters[i] = [d]

    # Определяем начальное расстояние между кластерами
    dt = 0
    while dt < size:
        n = len(clusters)

        # Для каждой пары кластеров находим расстояние друг от друга
        distances = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                distances[f"{i},{j}"] = cl_dist(clusters[i], clusters[j], dist)

        # Записываем признак пары кластеров и расстояние пары с самым маленьким расстоянием
        sij, dt = sorted(distances.items(), key=lambda x: x[1])[0]
        # Разбиваем на i, j
        ij = sij.split(',')
        # Объединяем кластеры i и j
        clusters = unify(clusters, int(ij[0]), int(ij[1]))

    return clusters


def unify(clusters: list, i: int, j: int) -> list:
    """
    Объединяет кластеры i и j в класте под номером i
    :param clusters: Все кластеры
    :param i: Номер первого кластера для объединения
    :param j: Номер второго кластера для объединения
    :return:
    """
    new_cl = clusters[i] + clusters[j]
    clusters[i] = new_cl
    del clusters[j]
    for k in range(j + 1, len(clusters) + 1):
        clusters[k - 1] = clusters.pop(k)
    return clusters


def euclidean_dist(x, y):
    """
    Вычисляет Евклидово расстояние
    :param x:
    :param y:
    :return:
    """
    return sum((xi-yi)**2 for xi, yi in zip(x, y))**(1/2)


def cl_center(c: list) -> list:
    """
    Вычисляет центр кластера (среднее по координатам)
    :param c: Кластер
    :return: Центр кластера (точка)
    """
    return [sum(x[i] for x in c) / len(c) for i in range(len(c[0]))]


def cl_dist(c1: list, c2: list, dist):
    """
    Вычисляет расстояние между кластерами
    :param c1: Кластер первый
    :param c2: Кластре второй
    :param dist: Функция, с помощью которой меряется расстояние
    """
    return dist(cl_center(c1), cl_center(c2))
