from random import randint
from numpy.linalg import solve as gauss_method
import numpy as np
from math import exp
from dsmltf import scale, mult_r_squared, mult_predict, dot

def regression(X, y):
    n = len(y)  # Количество наблюдений
    M = []  # левая часть СЛАУ для регрессии
    b = []  # правая часть СЛАУ для регрессии

    # Добавляем первую строку в матрицу M и элемент в вектор b
    M.append([sum(x) for x in X] + [n])     # Суммы по столбцам + количество: sum(X[0])*beta_0 + sum(X[1])*beta_1 + ... + sum(X[m-1])*beta_(m-1) + n*alpha
    b.append(sum(y))                        # Сумма по целевой переменной:    sum(y)

    # Заполняем матрицу M и вектор b для каждого наблюдения
    for _, xl in enumerate(X):
        # Считаем скалярные произведения с xl для каждого X[i] - это коэфициенты для beta_i.
        M.append([dot(x, xl) for x in X] + [sum(xl)])
        # Считаем скалярное произведение вектора наблюдений и xl
        b.append(dot(y, xl))

    # Вычисляем коэффициенты регрессии с помощью метода Гаусса
    beta = gauss_method(np.array(M, dtype="float64"), np.array(b, dtype="float64"))
    return beta  # Возвращаем коэффициенты регрессии, beta[-1] - это alpha

def solve(data: list):

    for i in range(30):
        #print(f"{i + 1}. Рейтинг: {data[i][0]}, Сюжет: {data[i][1]}, Автор: {data[i][2]}, Краткое описание: {data[i][3]}, Стиль письма: {data[i][4]}, Грамотность: {data[i][5]}, Жанр: {data[i][6]}, Результат: {data[i][7]}")
        print(
            f"{i + 1}. Рейтинг: {data[i][0]}, Сюжет: {data[i][1]}, Автор: {data[i][2]}, Стиль письма: {data[i][3]}, Жанр: {data[i][4]}, Результат: {data[i][5]}")
    print("\n")
    k = len(data[0]) - 1 # Количество критериев

    # Готовим данные для регрессии
    X = [[] for _ in range(k)]                      # Список для параметров
    y = []                                          # Список для результатов (наблюдений)

    # Масштабируем (прошкалируем) данные
    scaled_data = scale(data)

    # Приведём данные к нужному для регрессии виду
    for i in range(len(scaled_data) - 10):
        for j in range(k):
            X[j].append(scaled_data[i][j])          # Заполняем признаки
        y.append(scaled_data[i][-1])                # Добавляем значение результата в массив

    # Вычисляем коэффициенты регрессии
    beta = regression(X, y)
    print(f"Коэффициенты регрессии: {beta}")

    # Вычисляем R-квадрат ошибки
    r_squared = mult_r_squared([item[:-1] for item in scaled_data[-10:]], y, beta)

    # Тестируем на тестовом наборе данных
    for i in range(15, 30):
        prediction = mult_predict(scaled_data[i][:-1], beta)        # Делаем предсказание
        answer = 1 if exp(prediction) / (1 + exp(prediction)) > 0.5 else 0  # Преобразуем предсказание в бинарный ответ
        if data[i][-1] != answer:  # Проверяем правильность предсказания
            print(f"Ошибка предсказания: ожидалось {data[i][-1]}, получено {answer}, данные: {data[i]}, номер элемента выборки: {i}")

    print(f"Ошибка R-квадрата: {r_squared}")  # Выводим R-квадрат ошибки