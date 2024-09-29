import math

from matplotlib import pyplot

from supporting import integrator

def fourierSeriesApproximation(func, N, x, T):
    a0 = 2/T * integrator.integral(func, 0, T)
    res = a0/2

    for i in range(1, N + 1):
        a = 2/T * integrator.integral(lambda first: func(first) * math.cos(i * first), 0, T)
        b = 2/T * integrator.integral(lambda second: func(second) * math.sin(i * second), 0, T)

        res += a * math.cos(i * x) + b * math.sin(i * x)

    return res


def generateX():
    print("Введите левую границу:")
    x_start = float(input())
    print("Введите правую границу:")
    x_end = float(input())
    print("Введите щаг:")
    step = float(input())

    listX = []
    x = x_start
    while x < x_end:
        listX.append(x)
        x += step

    return listX

def solve(func):
    print("Введите число гармоник:")
    N = int(input())

    x = generateX()
    T = 2 * math.pi

    y_approximated = []
    for i in range(len(x)):
        y_approximated.append(fourierSeriesApproximation(f, N, x[i], T))

    y = []
    for i in range(len(x)):
        y.append(func(x[i]))

    pyplot.grid()
    pyplot.plot(x, y_approximated, marker='o', markersize=2)
    pyplot.show()