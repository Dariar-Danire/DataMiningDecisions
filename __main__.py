from lab1 import task8
import time

if __name__ == '__main__':
    start_time = time.time()

    #N = int(input("Введите количество чисел Фибоначчи: "))
    #a = list(task7.solve(N))
    #print(a)

    N = int(input("Введите количество цифр: "))
    print(task8.solve(N))

    print("\nEnd time: ", time.time() - start_time)