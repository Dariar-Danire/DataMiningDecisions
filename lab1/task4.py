# Напишите генератор простого числа, ближайшего к введенному натуральному числу.
import random



def solve(num):
    potentially_simple_1 = num
    potentially_simple_2 = num

    # 661 662 663 664 665 666 667 668 669 670 671 672 673

    for _ in range(1000):
        potentially_simple_1 += 1
        potentially_simple_2 -= 1

        a = is_prime(potentially_simple_1)
        b = is_prime(potentially_simple_2)

        if a and b and potentially_simple_1 > 0 and potentially_simple_2 > 0:
            L = [potentially_simple_1, potentially_simple_2]
            print(random.choice(L))
            break
        elif a and potentially_simple_1 > 0:
            print(potentially_simple_1)
            break
        elif b and potentially_simple_2 > 0:
            print(potentially_simple_2)
            break



def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True