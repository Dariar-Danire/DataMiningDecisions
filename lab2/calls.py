from lab2 import task1
from lab2 import task2

def call_task(number: int):
    match number:
        case 1:
            print("За скорость выкладки плитки самого лучшего плиточника в компании берём 8.")
            x = int(input("Введите число удачных исходов в выборке x: "))

            task1.solve(x)
        case 2:
            task2.solve()