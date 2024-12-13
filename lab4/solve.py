import math
from time import time
from matplotlib import pyplot

from dsmltf import gradient_descent, minimize_stochastic

# Список для начальных значений x
x = []

# Список коэфициентов, которые в методе Фурье в косинусах и синусах
base = [2 * math.pi * (i / 500) for i in range(500)]


# Находит значение аппроксимирующего многочлена в точке base[k] с коэфициентами a
def furie(k, a):
    return a[0] + a[1]* math.cos(base[k]) + a[2]* math.sin(base[k]) + a[3]* math.cos(2 * base[k]) + a[4]* math.sin(2 * base[k])

# Функция ошибок для пакетного градиентного спуска
def F(a) -> float:
    return sum([(x[i] - furie(i, a)) ** 2 for i in range(500)])

# Функция ошибок для стохастического градиентного спуска
# Почему здесь без суммы?
def f(i, a):
    return (x[i]-furie(i,a))**2


def solve():
    n = 500                             # Размерность вектора
    k = 12                              # Мой номер в журнале
    dt = 2 * math.pi / 1000
    L = k / 100
    omega = 1000 / k
    global x

    x = [0, (-1) ** k * dt]
    for i in range(2, n):
        x.append(x[i - 1] * (2 + dt * L * (1 - x[i - 2] ** 2))
                 - x[i - 2] * (1 + dt ** 2 + dt * L * (1 - x[i - 2] ** 2))
                 + dt ** 2 * math.sin(omega * dt))

    # Методом пакетного градиентного спуска подбобрать номера (частоты) и коэффициенты разложения Фурье из двух гармоник (пять параметров), аппроксимирующего функцию x[i].
    a_batch = gradient_descent(F, [0]*5, 500, 0.05, 0.01, 1e-5)
    time_batch = time()

    # Сделать то же самое методом стахастического градиентного спуска
    a_stochastic = minimize_stochastic(f, [i for i in range(500)], [0]*500, [0]*5, 1e-2, 1000)
    time_stochastic = time()

    # Коэфициенты a_batch и a_stochastic
    print(f"Коэфициенты, вычисленные с помощью пакетного градиентного спуска: {a_batch[0]}\tЗначение функции: {a_batch[1]}")
    print(f"Коэфициенты, вычисленные с помощью стохастического градиентного спуска: {a_stochastic[0]}\tЗначение функции: {a_stochastic[1]}")

    # Сравниваем время воспроизведения алгоритмов градиентного спуска
    print(f"\nПакетный градиентный спуск выполнен за {time_stochastic - time_batch} секунд.",
          f"\nСтохастический градиентный спуск выполнен за {time() - time_stochastic} секунд.")

    # Вычисляю x-ы для аппроксимированных функций
    res_batch      = [furie(i, a_batch[0]) for i in range(500)]
    res_stochastic = [furie(i, a_stochastic[0]) for i in range(500)]

    # Строю график
    pyplot.title(f"График функции при k = {k}")
    pyplot.plot(base, x, label='Изначальная функция', marker='o', markersize=0.5)
    pyplot.plot(base, res_batch, label=f'Градиентный спуск', linestyle='-')
    pyplot.plot(base, res_stochastic, label=f'Стохатический градиентный спуск', linestyle='-')
    pyplot.legend()
    pyplot.show()
