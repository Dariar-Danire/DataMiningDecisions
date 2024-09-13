# Для произвольно заданного двухуровневого списка из целых, вещественных и комплексных чисел, выберите только
# комплексные числа и запишите их в кортеж.

def solve(a : list):
    result = []
    contrast = 1 + 2j

    for i in range(len(a)):
        for j in range(len(a[i])):
            if type(a[i][j]) == type(contrast):
                result.append(a[i][j])

    print(tuple(result))