import csv

# Структура файла: ID,      Длина чашелистика,      Ширина чашелистика,     Длина лепестка,     Ширина лепестка,    Вид ириса
# Структура файла: ID,      SepalLengthCm (0),      SepalWidthCm (1),       PetalLengthCm (2),  PetalWidthCm (3),   Species
def parseCSV_Irises(path_to_file) -> list:
    f = open(path_to_file)
    dataset = []

    for str_i in csv.reader(f, delimiter=','):
        try:
            data_i = [float(str_i[1]), float(str_i[2]), float(str_i[3]), float(str_i[4])]
            dataset.append((data_i, str_i[5]))
        except:
            continue

    return dataset

def parseCSV_Earthquaces(path_to_file) -> list:
    f = open(path_to_file)
    dataset = []

    for str_i in csv.reader(f, delimiter=','):
        try:
            data_i = [float(str_i[1]), float(str_i[2]), float(str_i[4])] # Широта, долгота и магнитуда соответственно
            dataset.append(data_i)
        except:
            continue

    print(f"max_latitude: {max_latitude}, max_longitude: {max_longitude}")
    return dataset