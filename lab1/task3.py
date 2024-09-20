# Напишите код, заменяющий серию одинаковых гласных в вводимой строке на одну эту гласную.
from re import sub
from re import IGNORECASE

def solve(source_str):

    vowels = ['a', 'e', 'i', 'o', 'u']

    for word in vowels:
        pattern = '[' + word + ']+'
        source_str = sub(pattern, word, source_str, flags=IGNORECASE)

    return source_str