# С помощью итератора из упражнения 7, найдите индекс первого элемента последовательности
# частичных сумм ряда Фибоначчи,содержащего БОЛЕЕ, чем заданное число, значащих цифр.

from lab1 import task7

def solve(n: int):
    cnt = 0
    for num in list(task7.solve(50)):
        if len(str(num)) > n:
            return cnt
        cnt += 1
    raise Exception("A number was not found in the specified range!")