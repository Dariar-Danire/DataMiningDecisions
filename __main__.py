from lab1 import task7
import time

if __name__ == '__main__':
    start_time = time.time()

    N = int(input("Введите количество чисел Фибоначчи: "))
    print(list(task7.solve(N)))

    print("\nEnd time: ", time.time() - start_time)