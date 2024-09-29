import numpy



def gauss(M, b):
    for k in range(M.shape[0] - 1):
        # поиск строки с максимальным элементом
        max_elem = 0
        str = 0
        for i in range(k, M.shape[0]):
            if abs(M[i, k]) > abs(max_elem):
                max_elem = M[i, k]
                str = i
        # меняем местами строки квадратной матрицы
        change = numpy.repeat(M[k], 1)
        M[k], M[str] = M[str], change
        # меняем местами элементы вектора-столбца
        change = numpy.repeat(b[k], 1)
        b[k], b[str] = b[str], change
        # делим полученную строку на max_elem
        M[k] = M[k] / max_elem
        b[k] = b[k] / max_elem
        # домножаем строку на коэффициенты и вычитаем ее из остальных строк
        for i in range(k + 1, M.shape[0]):
            factor = M[i, k]
            M[i] = M[i] - M[k] * factor
            b[i] = b[i] - b[k] * factor

        # находим аргументы уравнений
    arg = [b[b.shape[0] - 1] / (M[M.shape[0] - 1, M.shape[0] - 1])]
    for i in range(M.shape[0] - 2, -1, -1):
        n = b[i]
        for j in range(len(arg)):
            n = n - arg[j] * M[i, M.shape[0] - 1 - j]
        arg.append(n)

    # переворачиваем значения в списке
    otv = []
    for i in reversed(arg): otv.append(i)
    return otv