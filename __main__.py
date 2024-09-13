from lab1 import task6
import time

if __name__ == '__main__':
    start_time = time.time()
    a = [[1 + 2j, 4, 2.7, 9 - 2j],
         [3.5, 7, 10 + 8j, 2],
         [5, 2 - 1j, 19.5, 3],
         [3 + 4j, 6 + 7j, 5, 3.9]]
    task6.solve(a)
    print("\nEnd time: ", time.time() - start_time)