from lab2 import calls
import time

if __name__ == '__main__':
    start_time = time.time()

    task_number = int(input("Введите номер задачи: "))
    calls.call_task(task_number)

    print("\nEnd time: ", time.time() - start_time)

