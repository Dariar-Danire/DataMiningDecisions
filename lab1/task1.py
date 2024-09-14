# Напишите модуль для нахождения НОД числа 8 и заданного 10-значного числа,
# не используя арифметические операции, но с использованием функций пользователя.


def binary_gcd(num1, num2):
    shift = 0

    # НОД(0, num2) = n; НОД(num1, 0) = m.
    if num1 == 0 or num2 == 0:
        return num1 | num2

    # Если num1, num2 чётные, тогда НОД(num1, num2) = 2 * НОД(num1 / 2, num2 / 2).
    # Пусть shift := lg K, где K наибольшая степень 2 такая, что оба числа
    # целиком делятся на 2 в степени K.
    while (num1 | num2) & 1 == 0:
        shift += 1
        num1 >>= 1
        num2 >>= 1

    # Если num1 чётное, тогда НОД(num1 / 2, num2)
    while num1 & 1 == 0:
        num1 >>= 1

    # Считаем, что num1 нечётное
    while num2 != 0:

        while num2 & 1 == 0:    # Если num2 чётное, тогда НОД(num1, num2) = НОД(num1, num2 / 2)
            num2 >>= 1

        if num1 > num2:
            # меняем их местами
            num1, num2 = num2, num1
        #теперь первое число меньше второго, вычитаем
        num2 -= num1

    # возвращаем число, перед этим сдвинув его биты на shift
    return num1 << shift