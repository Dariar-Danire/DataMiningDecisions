from lab1 import task1

def solve():
    try:
        a = 8
        b = int(input("Введите любое десятизначное число: "))

        if len(str(b)) < 10 or len(str(b)) > 10:
            raise Exception("The number must be ten digits!")

        nod = task1.gcd_8(b)
        print(nod)
    except Exception as e:
        print("Error!", repr(e))