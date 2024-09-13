# Напишите код, заменяющий серию одинаковых гласных в вводимой строке на одну эту гласную.

def solve(source_str):
    source_str = source_str.lower()

    vowels = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    i = 0

    while i < (len(source_str) - 1):
        a = source_str[i]
        b = source_str[i + 1]

        if i == (len(source_str) - 2) and source_str[i + 1] == source_str[i]:
            cnt += 2
            source_str = source_str.replace((source_str[i] * cnt), source_str[i], 1)
            print(source_str)

        elif source_str[i] in vowels and source_str[i + 1] == source_str[i]:
            cnt += 1

        elif source_str[i] in vowels and source_str[i + 1] != source_str[i] and cnt > 0:
            cnt += 1

            source_str = source_str.replace((source_str[i] * cnt), source_str[i], 1)

            i -= (cnt - 1)
            cnt = 0
            print(source_str)

        i += 1

    print(source_str)