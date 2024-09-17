from lab1 import task1
#from supporting.vector import Vector
import time

if __name__ == '__main__':
    start_time = time.time()

    # Задача 3
    #str = input("Введите строку с повторяющимися гласными: ")
    #task3.solve(str)

    # Задача 4
    #try:
    #    num = int(input("Введите число: "))
    #    n = int(input("Введите диапазон поиска: "))

    #    prime_num = task4.solve(num, n)

    #    if prime_num == -404:
    #        raise Exception("A prime number was not found in the specified range!")

    #    print(prime_num)

    #except Exception as e:
    #    print("Error!", repr(e))


    # Задача 6
    #A = [[1 + 2j, 5, 2 + 6j, 6.7],
    #     [2.7, 9, 4 + 5j, 8 + 9j],
    #     [10, 14.5, 18, 1 + 7j],
    #     [4 + 2j, 5.0, 8, 2.8]]
    #print(task6.solve(A))

    # Задача 7
    #N = int(input("Введите количество чисел Фибоначчи: "))
    #a = list(task7.solve(N))
    #print(a)

    # Задача 8
    #N = int(input("Введите количество цифр: "))
    #print(task8.solve(N))

    # Задача 9
    #frac1 = task9.Frac(10, 3)
    #frac2 = task9.Frac(2, 3)

    #frac1.flip_over()
    #frac1.print()
    #print('\n')

    #frac3 = frac1.summ(frac2)
    #frac4 = frac1.multiplication(frac2)

    #frac3.print()
    #print('\n')
    #frac4.print()

    # Задача 11
    #a = Vector(3, -1, -2)
    #b = Vector(1, 2, -1)

    #result = task11.vector_product(a, b)

    #result.print()

    # Задачи 1-2
    #try:
    #    a = 8
    #    b = int(input("Введите любое десятизначное число: "))

    #    if len(str(b)) < 10 or len(str(b)) > 10:
    #        raise Exception("The number must be ten digits!")

    #    nod = task1.gcd_8(b)
    #    print(nod)
    #except Exception as e:
    #    print("Error!", repr(e))

    #str = input("Введите исходную строку: ")
    #task3.solve(str)

    print("\nEnd time: ", time.time() - start_time)

