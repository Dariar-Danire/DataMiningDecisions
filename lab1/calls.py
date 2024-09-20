from lab1 import task2
from lab1 import task3
from lab1 import task4
from lab1 import task6
from lab1 import task7
from lab1 import task8
from lab1 import task9
from lab1 import task11
from supporting import vector

def call_task(number: int):
    match number:
        case 1:
            print("Решение задачи №1 (поиск НОД числа 8 и введённого числа):\n")

            task2.solve()
        case 2:
            print("Решение задачи №2 (поиск НОД числа 8 и введённого числа, но с контролем ввода):\n")

            task2.solve()
        case 3:
            print("Решение задачи №3 (сокращение повторяющихся гласных):\n")

            str = input("Введите исходную строку: ")
            str = task3.solve(str)
            print(str)
        case 4:
            print("Решение задачи №4 (поиск ближайшего простого числа):\n")

            try:
                num = int(input("Введите число: "))
                n = int(input("Введите диапазон поиска: "))

                prime_num = task4.solve(num, n)
            except Exception as e:
                print("Error!", repr(e))
            else:
                print("Ближайшее простое число:", prime_num)
        case 5:
            print("Задача не решена.")
        case 6:
            print("Решение задачи №6 (выбор комплексных чисел из двухуровневого списка):\n")

            A = [[1 + 2j, 5, 2 + 6j, 6.7],
                [2.7, 9, 4 + 5j, 8 + 9j],
                [10, 14.5, 18, 1 + 7j],
                [4 + 2j, 5.0, 8, 2.8]]
            print(task6.solve(A))
        case 7:
            print("Решение задачи №7 (вывод N чисел Фибоначчи):\n")

            N = int(input("Введите количество чисел Фибоначчи: "))
            a = list(task7.solve(N))
            print(a)
        case 8:
            print("Решение задачи №8 (вывод индекса первого числа, разрядностью превышающего N):\n")

            try:
                n = int(input("Введите количество цифр N: "))
                N = int(input("Введите диапазон поиска: "))

                result = task8.solve(n, N)
            except Exception as e:
                print("Error!", repr(e))
            else:
                print(result, "(нумерация идёт с 0, поскольку в задании просят именно индекс)")
        case 9:
            print("Решение задачи №9 (класс Frac с простыми дробями):\n")

            # Создаём 2 исходных дроби
            frac1 = task9.Frac(10, 3)
            frac2 = task9.Frac(2, 3)

            # Переворачиваем 1 дробь
            frac1.flip_over()
            frac1.print()
            print('\n')

            # Складываем 2 дроби и умножаем их же. Записываем результаты в новые переменные
            frac3 = frac1.summ(frac2)
            frac4 = frac1.multiplication(frac2)

            # Выводим результаты на экран
            frac3.print()
            print('\n')
            frac4.print()
        case 10:
            print("Задача не решена.")
        case 11:
            print("Решение задачи №11 (нахождение векторного произведения двух векторов):\n")

            a = vector.Vector(3, -1, -2)
            b = vector.Vector(1, 2, -1)

            result = task11.vector_product(a, b)

            result.print()
        case 12:
            print("Задача не решена.")