from lab6.kNearestNeighbours import solve_irises, solve_earthquaces

def knn_for_six_lab():
    n = int(input("1 - Задача с ирисами \n2 - Задача с землетрясениями \nЧто запустить? \n"))

    match n:
        case 1:
            solve_irises()
        case 2:
            solve_earthquaces()