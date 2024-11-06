from dsmltf import k_neighbours_classify, knn_classify
from lab6.parseCSVToDataset import parseCSV_Earthquaces

def solve_earthquaces():
    k = 12

    source_dataset = parseCSV_Earthquaces("C:/Users/Дарья/Documents/Университет/ИАД/DataMiningDecisions/lab6/datasets/italy_earthquakes_from_2016-08-24_to_2016-11-30.csv")

    # Делаем из датасета 2 выборки:
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
    accuracy_1dp = [dict_1dp[i][0] / dict_1dp[i][1] for i in range(1, k + 1)]
    accuracy_0dp = [dict_0dp[i][0] / dict_0dp[i][1] for i in range(1, k + 1)]

    # Вычисляем нучшие k
    best_k_1dp = accuracy_1dp.index(max(accuracy_1dp)) + 1
    best_k_0dp = accuracy_0dp.index(max(accuracy_0dp)) + 1

    # Италия, 39-44 с.ш. 10-16 в.д.
    latitude, longitude = map(lambda x: float(x), input("Введите широту и долготу: ").split())
    print(f"Магнитуда, предсказанная на выборке, округлённой до 1 знака после запятой: {knn_classify(best_k_1dp, dataset_1dp, (latitude, longitude))}")
    print(f"Магнитуда, предсказання на выборке, округлённой до целого числа: {knn_classify(best_k_0dp, dataset_0dp, (latitude, longitude))}")
