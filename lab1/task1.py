# Напишите модуль для нахождения НОД числа 8 и заданного 10-значного числа,
# не используя арифметические операции, но с использованием функций пользователя.


# Т. к. первое число у нас всегда фиксированное - 8, нам достаточно перебрать случаи
# с окончанием двоичного представления num на окончание 1, 0, 00, 000.
# Это 4 единственно возможных НОД в этой задаче.
def gcd_8(num2):
    b = str(bin(num2))

    if b[-1] == '1':
        return 1
    elif b[-3:] == '000':
        return 8
    elif b[-2:] == '00':
        return 4
    elif b[-1] == '0':
        return 2