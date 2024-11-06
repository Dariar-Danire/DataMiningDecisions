from dsmltf import k_neighbours_classify, knn_classify

def find_best_k(dataset, k = 15):
    """
    Находит лучшее количество соседей для метода k ближайших соседей
    :param dataset: список кортежей вида ([признак_1, признак_2, ..., признак_n], метка)
    :param k: конечное число соседей
    :return: лучшее k для этой выборки
    """
    # Вычисляю словарь вида (количество правильных предсказаний, общее количество предсказаний) для каждого k
    dict_k = k_neighbours_classify(k, dataset)

    # Вычисляю проценты точности для каждого k
    accuracy = [dict_k[i][0] / dict_k[i][1] for i in range(1, k + 1)]

    # Выбираю среди них k с максимальным процентом точности
    best_k = accuracy.index(max(accuracy)) + 1

    return best_k

def test_knn_dataset(dataset, k):
    """
    Находит количество верных предсказаний для переданной выборки
    :param dataset: список кортежей вида ([признак_1, признак_2, ..., признак_n], метка)
    :param k: количество ближайших соседей для предсказания методом KNN
    :return:
    """
    correct_predictions = 0 # Счётчик правильных предсказаний

    for data_i in dataset:
        marks, fact_label = data_i[0], data_i[1]

        other_data = [other_item for other_item in dataset
                      if other_item != data_i]

        predicted_label = knn_classify(k, other_data, marks)

        if predicted_label == fact_label:
            correct_predictions += 1

    return correct_predictions, len(dataset)