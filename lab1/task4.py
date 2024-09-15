# Напишите генератор простого числа, ближайшего к введенному натуральному числу.
import random



def solve(num, n=1000):
    potentially_prime_1 = num
    potentially_prime_2 = num

    # 661 662 663 664 665 666 667 668 669 670 671 672 673

    for _ in range(n):
        potentially_prime_1 += 1
        potentially_prime_2 -= 1

        a = is_prime(potentially_prime_1)
        b = is_prime(potentially_prime_2)

        if a and b and potentially_prime_1 > 0 and potentially_prime_2 > 0:
            L = [potentially_prime_1, potentially_prime_2]
            return random.choice(L)
        elif a and potentially_prime_1 > 0:
            return potentially_prime_1
        elif b and potentially_prime_2 > 0:
            return potentially_prime_2
    return -404

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True