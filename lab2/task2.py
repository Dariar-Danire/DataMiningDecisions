# Задание №2:
# Определите наилучшее полиномиальное приближение для процесса суточного изменения цены опциона (выберите любой опцион на любой бирже).
# Рассчитайте p-значение для этого приближения и мощность проверки.
import math
import numpy
from supporting.Gauss import gauss
from matplotlib import pyplot


def solve(x_hat, t):
    # Находим коэфициенты для статистической гипотезы
    a = approx_poly(x_hat, t, 2)

    # Вычисляем x
    x = f(t, a)

    # Вычисляем стандартное отклонение
    sigma = find_sigma(x, x_hat)
    print("sigma =", sigma)

    # Вычисляем среднее отклонение
    mu = find_mu(x, x_hat)
    print("mu =", mu)

    # Вычисляем стандартное отклонение
    sigma = find_sigma(x, t)
    print("sigma =", sigma)

    # Вычисляем максимальное по модулю отклонение от среднего
    max_e = 0
    for i in range(len(x)):
        if math.fabs(x[i] - x_hat[i]) > math.fabs(max_e):
            max_e = (x[i] - x_hat[i])

    print("Максимальное по модулю отклонение от среднего = ", max_e)

    # Вычисляем p-значение
    p_max = p_value(max_e, mu, sigma)
    print("p_value =", p_max)

    # Вычисляем мощность проверки
    w = 1 - rho_norm(max_e, mu, sigma)
    print("Мощность првоерки W =", w)
    # Высвечиваем график
    # Из-за очень большой разницы между фактическими значениями и найденными в ходе аппроксимации график не строится
    pyplot.plot(t, x, 'b-', label ='Approx')
    pyplot.plot(t, x_hat, 'rx', label='Fact')
    pyplot.legend()
    pyplot.show()


# Статистическая гиотеза и маска функции в виде полинома
def f(x_hat, a: list):
    result = []

    for i in range(len(x_hat)):
        res_i = 0

        for k in range(len(a)):
            res_i += a[k] * (x_hat[i] ** k)
        result.append(res_i)

    return result

# Функция для полиномиальной аппроксимации
# x - это, видимо, сам список значений
# t - это список временных меток к каждому из значений
# r - порядок полинома
# В итоге получаем список коэффициентов для статистической гипотезы
def approx_poly(x,t,r): # в списке x любые числа
    M = [[] for _ in range(r+1)]
    b = []
    for l in range(r+1):
        for q in range(r+1):
            M[l].append(sum(list(map(lambda z: z**(l+q), t)))) # Для каждого эллемента t выполняем lambda z и суммируем с предыдущими результатами
        b.append(sum(xi*ti**l for xi,ti in zip(x,t)))
    a = gauss(numpy.array(M), numpy.array(b)) # Это наши коэфициенты a_0, a_1, ..., a_n
    return a

# Нормальное распределение - плотность вероятности
def rho_norm(x, mu=0, s=1.0):
    return 1/math.sqrt(2*math.pi*s) *math.exp(-(x-mu) **2/2/s**2)

# Нормальное распределение - функция распределения
def f_norm(x, mu=0, s=1):
    return(1+math.erf((x-mu)/math.sqrt(2)/s))/2

# p-значение (вероятность ошибки первого рода)
def p_value(x, mu=0, s=1.0):
    if x >=mu:
        return 2*(1-f_norm(x, mu, s))
    else:
        return 2*f_norm(x, mu, s)

def find_mu(x, x_hat):
    mu = 0
    for i in range(len(x_hat)):
        mu += x[i] - x_hat[i]

    mu /= len(x_hat)
    return mu

def find_sigma(x, x_hat):
    n = len(x)
    if len(x) != len(x_hat):
        raise ValueError("x and t must be the same length")

    # Среднее арифметическое между всеми значениями e[i] = x[i] - x_hat[i]
    mu = 0
    for i in range(len(x)):
        mu += (x[i] - x_hat[i])
    mu /= len(x)

    # Находим итоговое σ = √((Σ(x - μ)^2) / n)
    sum_e = 0
    for i in range(len(x_hat)):
        sum_e += (x[i] - x_hat[i] - mu) ** 2 # x[i] - x_hat[i] = e[i]

    sigma = math.sqrt(sum_e / n)

    return sigma


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
#                                               Экспоненциальная аппроксимация
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\

# Экспоненциальная маска, статистическая гипотеза
def f_new(t: list, A, b: float):
    result = []
    for t_i in t:
        result.append(A * math.exp(b*t_i))

    return result

# Функция для экспоненциальной аппроксимации
def approx_exp(x,t): # в списке x только положительные числа
    n = len(x)
    y = list(map(math.log, x))
    sum_t, sum_y = sum(t), sum(y)
    sum_t2 = sum(ti**2 for ti in t)
    sum_yt = sum(ti*yi for ti,yi in zip(t,y))
    a = (sum_yt*sum_t - sum_y*sum_t2)/ (sum_t**2 - sum_t2*n)
    b = (sum_y*sum_t - sum_yt*n)/ (sum_t**2 - sum_t2*n)
    return math.exp(a),b # выдаются параметры A и b

def solve_e(x_hat, t):
    A, b = approx_exp(x_hat, t)
    x = list(map(lambda z: A * math.exp(b * z), t))
    print('A =', A,' b =', b)

    mu = find_mu(x, x_hat)
    print("mu =", mu)

    sigma = find_sigma(x, x_hat)
    print("sigma =", sigma)

    # Вычисляем максимальное по модулю отклонение от среднего
    max_e = 0
    for i in range(len(x)):
        if math.fabs(x[i] - x_hat[i]) > math.fabs(max_e):
            max_e = (x[i] - x_hat[i])

    print(max_e)

    p_max = p_value(max_e, mu, sigma)
    print("p_value =", p_max)

    w = 1 - rho_norm(max_e, mu, sigma)
    print("w =", w)

    pyplot.plot(t, x_hat,'rx', label ='Fact')
    pyplot.plot(t, x, 'b-', label ='Approx')
    pyplot.legend()
    pyplot.show()