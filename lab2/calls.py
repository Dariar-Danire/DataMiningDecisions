from lab2 import task1
from lab2 import task2

def call_task(number: int):
    match number:
        case 1:
            print("За скорость выкладки плитки самого лучшего плиточника в компании берём 8.")
            x = int(input("Введите число удачных исходов в выборке x: "))

            task1.solve(x)

        case 2:
            # почасовая статистика цен фьючерсов на золото с 27.09.2024 00:00:00 по 27.09.2024 23:00:00
            x = [2695.35,   2694.6,     2694.35,    2693.5,
                 2691.8,    2690.1,     2691.65,    2695.0,
                 2692.9,    2688.75,    2689.45,    2686.15,
                 2683.45,   2688.35,    2687.35,    2687.4,
                 2690.1,    2686.65,    2668.2,     2669.8,
                 2671.1,    2667.6,     2669.1,     2674.1]
            t = range(len(x))

            x = [11, 13, 20, 30, 50, 60]
            t = range(len(x))

            task2.solve_e(x, t)