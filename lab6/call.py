from lab6.knn_irises import solve_irises
from lab6.knn_earthquake import solve_earthquaces

def knn_for_six_lab():
    n = int(input("1 - Задача с ирисами \n2 - Задача с землетрясениями \nЧто запустить? \n"))

    match n:
        case 1:
            solve_irises()
        case 2:
            solve_earthquaces()
