from lab8.task1 import solve as solve_task1
from lab8.task2 import solve as solve_task2

def calling_task():
    n = int(input("1 - Решение задачи со студентами \n2 - Решение задачи про собеседование \nЧто вызвать?\n"))

    match n:
        case 1:
            solve_task1()
        case 2:
            solve_task2()
        case _:
            print("Такой задачи нет! Попробуйте ещё раз.")
            calling_task()
