from dsmltf import count_words
from nltk import pos_tag
from collections import defaultdict
from lab7.support_methods import parse_csv, test_bayes_f1, word_probabilities, test_bayes
from supporting.split_dataset import train_test_dataset_split


def solve():
    dataset = parse_csv("C:/Users/Дарья/Documents/Университет/ИАД/DataMiningDecisions/lab7/datasets/spam.csv")

    # Вычисляем количество спамных сообщений
    cnt_spam = len([i for i in dataset if i[1]])
    cnt_ham = len(dataset) - cnt_spam

    # Делим на тестовую и тренировочную выборку
    train_dataset, test_dataset = train_test_dataset_split(dataset)

    ##############################    РАБОТАЕМ С ТРЕНИРОВОЧНОЙ ВЫБОРКОЙ   ############################################################
    # Определяем тренировочные данные
    training_set = count_words(train_dataset)

    # Определяем словарь с определением части речи
    tagged_keys = pos_tag(training_set.keys())

    # Фильтруем данные(без прилогательных)
    training_set = defaultdict(lambda: [0, 0], {key: training_set[key] for key, tag in tagged_keys if tag not in ('JJ', 'JJR', 'JJS')})

    # Определяем самые часто встречающиееся слова в спаме
    words = sorted(training_set, key=lambda x: training_set[x][0] if len(x) >= 5 else 0)[-7:]
    words = [(i, training_set[i][0]/cnt_spam, training_set[i][1]/cnt_ham if training_set[i][1]/cnt_ham else 0.01)  for i in words]

    ###############################    РАБОТАЕМ С ТЕСТОВОЙ ВЫБОРКОЙ   ##############################################################
    # Пробуем без сглаживания
    correct_predictions_1, all_predictions_1 = test_bayes(words, test_dataset)
    res_1 = round(correct_predictions_1 / all_predictions_1, 4) * 100

    # Проводим сглаживание
    words = word_probabilities([(i[0], training_set[i[0]][0], training_set[i[0]][1]) for i in words], cnt_spam, cnt_ham, 400)
    correct_predictions_2, all_predictions_2 = test_bayes(words, test_dataset)
    res_2 = round(correct_predictions_2 / all_predictions_2, 4) * 100

    # Выводим результаты
    print(f"Точность без сглаживания:\t{correct_predictions_1} / {all_predictions_1} ({res_1})")
    print(f"Точность со сглаживанием:\t{correct_predictions_2} / {all_predictions_2} ({res_2})")


