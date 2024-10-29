# Структура файла: ID,      Длина чашелистика,      Ширина чашелистика,     Длина лепестка,     Ширина лепестка,    Вид ириса
# Структура файла: ID (0),  SepalLengthCm (1),      SepalWidthCm (2),       PetalLengthCm (3),  PetalWidthCm (4),    Species (5)

# Виды ирисов в файле: Iris-setosa, Iris-versicolor, Iris-virginica

from lab6.parseCSVToDataset import parseCSV_Irises, parseCSV_Earthquaces
from dsmltf import knn_classify, principal_components, genser, k_neighbours_classify

def solve_irises():

    # Скорректировать ещё формат данных в датасете
    dataset = parseCSV_Irises("C:/Users/Дарья/Documents/Университет/ИАД/DataMiningDecisions/lab6/datasets/Iris.csv")
    dataset_data = [i[0] for i in dataset]
    dataset_labels = [i[1] for i in dataset]

    # Надо на тест и трен разделить, а потом высчитать f1-метрику на основе тестовой выборки. А на основе трен обучать

    for k in range(1, 13):
        source_label_4 = knn_classify(k, dataset, [5.9, 3.0, 5.1, 1.8]) # +++
        print(source_label_4)

        # Снизить размерность датасета до 2 признаков методом PCA
        new_dataset_pca = principal_components(dataset_data, 2)
        dataset_pca = [(data_i, label_i) for data_i, label_i in zip(new_dataset_pca, dataset_labels)]
        pca_label_2 = knn_classify(k, dataset_pca, [5.9, 3.0, 5.1, 1.8])
        print(pca_label_2)

        # Снизить размерность до 2 признаков методом обобщённой сериализации
        new_dataset_gs = genser(dataset_data, 2, )            # (!!!!!!!!) + словарь степеней для каждого признака
        dataset_gs = [(data_i, label_i) for data_i, label_i in zip(new_dataset_gs, dataset_labels)]
        gs_label_2 = knn_classify(k, dataset_gs, [5.9, 3.0, 5.1, 1.8])

        # Сравнить полученные в ходе предыдущих 3х классификаций результаты
        print(f"k = {k}\n")
        print(f"Метка (4-мерный датасет):\t{source_label_4}")
        print(f"Метка (2-мерный датасет, PCA):\t{pca_label_2}")
        print(f"Метка (2-мерный датасет, genser):\t{gs_label_2}\n\n")

def solve_earthquaces():
    k = 12

    source_dataset = parseCSV_Earthquaces("C:/Users/Дарья/Documents/Университет/ИАД/DataMiningDecisions/lab6/datasets/italy_earthquakes_from_2016-08-24_to_2016-11-30.csv")

    # Разбиваем датасет на 2 выборки:
    # в одной округляем магнитуды до 1 знака после зпятой,
    # в другой округляем до целого
    dataset_1dp = [(data_i[:-1], round(data_i[-1], 1)) for data_i in source_dataset]
    dataset_0dp = [(data_i[:-1], round(data_i[-1])) for data_i in source_dataset]

    print(dataset_1dp[0])
    print(dataset_0dp[0])

    # Находим словари с результатами knn для k = 1, 2, ..., 12
    dict_1dp = k_neighbours_classify(k, dataset_1dp[:100])
    dict_0dp = k_neighbours_classify(k, dataset_0dp[:100])

    # Проценты точности
    a_1dp = [dict_1dp[i][0] / dict_1dp[i][1] for i in range(1, k + 1)]
    a_0dp = [dict_0dp[i][0] / dict_0dp[i][1] for i in range(1, k + 1)]

    # Вычисляем нучшие k
    greetest_k_1dp = a_1dp.index(max(a_1dp)) + 1
    greetest_k_0dp = a_0dp.index(max(a_0dp)) + 1

    # Италия, 39-44 с.ш. 10-16 в.д.
    latitude, longitude = map(lambda x: float(x), input("Введите широту и долготу: ").split())
    print(f"Магнитуда, предсказанная на выборке, округлённой до 1 знака после запятой: {knn_classify(greetest_k_1dp, dataset_1dp, (latitude, longitude))}")
    print(f"Магнитуда, предсказання на выборке, округлённой до целого числа: {knn_classify(greetest_k_0dp, dataset_0dp, (latitude, longitude))}")
