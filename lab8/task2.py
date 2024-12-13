from dsmltf import build_tree_id3, classify, train_test_split

from lab8.support_methods import test_classify
from supporting.split_dataset import train_test_dataset_split


def solve():
    # Определяем входные данные
    dataset = [
        ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'no'}, False),
        ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Senior', 'lang': 'Python', 'tweets': 'yes', 'phd': 'yes'}, True),
        ({'level': 'Mid', 'lang': 'Java', 'tweets': 'yes', 'phd': 'no'}, False),
        ({'level': 'Mid', 'lang': 'C++', 'tweets': 'no', 'phd': 'yes'}, True),
        ({'level': 'Junior', 'lang': 'C++', 'tweets': 'yes', 'phd': 'no'}, False),
        ({'level': 'Senior', 'lang': 'Go', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Java', 'tweets': 'no', 'phd': 'no'}, True),
        ({'level': 'Mid', 'lang': 'Go', 'tweets': 'no', 'phd': 'yes'}, True),
        ({'level': 'Senior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Go', 'tweets': 'yes', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'Java', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Senior', 'lang': 'C++', 'tweets': 'yes', 'phd': 'no'}, False),
        ({'level': 'Junior', 'lang': 'C++', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'Python', 'tweets': 'yes', 'phd': 'yes'}, True),
        ({'level': 'Senior', 'lang': 'JavaScript', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'JavaScript', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'JavaScript', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Senior', 'lang': 'Ruby', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'Ruby', 'tweets': 'no', 'phd': 'yes'}, True),
        ({'level': 'Junior', 'lang': 'Ruby', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Senior', 'lang': 'Go', 'tweets': 'no', 'phd': 'yes'}, True),
        ({'level': 'Mid', 'lang': 'Go', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Go', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Senior', 'lang': 'PHP', 'tweets': 'yes', 'phd': 'no'}, False),
        ({'level': 'Mid', 'lang': 'PHP', 'tweets': 'no', 'phd': 'yes'}, True),
        ({'level': 'Junior', 'lang': 'PHP', 'tweets': 'yes', 'phd': 'no'}, False),

        ({'level': 'Senior', 'lang': 'Java', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Mid', 'lang': 'Java', 'tweets': 'no', 'phd': 'no'}, False),
        ({'level': 'Junior', 'lang': 'Java', 'tweets': 'yes', 'phd': 'yes'}, True),
        ({'level': 'Senior', 'lang': 'C++', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'C++', 'tweets': 'yes', 'phd': 'no'}, True),
    ]

    print(f"Количество записей в датасете: {len(dataset)}")

    # Делим на тренировочную и тестовую выборки
    train_dataset, test_dataset = train_test_dataset_split(dataset)

    # Строим ДПР (Дерево Принятия Решений)
    tree = build_tree_id3(train_dataset)

    # Находим количество верных предсказаний на тестовой выборке
    correct_predictions, all_predictions = test_classify(tree, test_dataset)

    # Выводим результаты
    res = round(correct_predictions / all_predictions, 4) * 100
    print(f"Результаты теста: {correct_predictions}/{all_predictions} ({res})")
