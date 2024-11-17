from dsmltf import classify


def test_classify(tree, dataset):
    """
    Находит количество верных предсказаний для переданной выборки
    :param tree: дерево принятия решений
    :param dataset: список данных для проверки
    :return: количество удачных предсказаний, общее количество предсказаний
    """
    correct_predictions = 0
    all_predictions = len(dataset)

    for data_i in dataset:
        marks, fact_label = data_i[0], data_i[1]

        predicted_label = classify(tree, marks)

        if predicted_label == fact_label:
            correct_predictions += 1

    return correct_predictions, all_predictions