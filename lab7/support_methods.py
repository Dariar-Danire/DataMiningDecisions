import csv
import nltk
from dsmltf import spam_probability, f1_score


def word_probabilities(counts: list[tuple], total_spams: int, total_non_spams: int, k=0.5) -> list[tuple]:
    return [(w, (spam + k) / (total_spams + 2*k),
             (non_spam + k) / (total_non_spams + 2*k))
            for w, spam, non_spam in counts]


def test_bayes_f1(words: list[tuple], dataset: list) -> float:
    true_positive, false_positive, false_negative = 0, 0, 0

    for i in dataset:
        match round(spam_probability(words, i[0])), i[1]:
            case 1, 1:
                true_positive += 1
            case 1, 0:
                false_positive += 1
            case 0, 1:
                false_negative += 1

    return f1_score(true_positive, false_positive, false_negative)

def test_bayes(words: list[tuple], dataset: list):
    correct_predictions = 0
    all_predictions = len(dataset)

    for data_i in dataset:
        marks, fact_label = data_i[0], data_i[1]

        predicred_label = round(spam_probability(words, marks))

        if predicred_label == fact_label:
            correct_predictions += 1

    return correct_predictions, all_predictions


def parse_csv(path):
    #nltk.download("averaged_perceptron_tagger_eng")

    f = open(path, encoding="UTF-8")
    dataset = []

    for str_i in csv.reader(f, delimiter=','):
        dataset.append((str_i[1], 1 if str_i[0] == "spam" else 0))

    return dataset  # Если что изменить кортежи на списки



"""
Код для проверки предсказаний с помощью F1-метрики:
    # Пробуем без сглаживания
    print(f"F1-метрика без сглаживания: {test_bayes_f1(words, test_dataset)}")

    # Проводим сглаживание
    words = word_probabilities([(i[0], training_set[i[0]][0], training_set[i[0]][1]) for i in words], cnt_spam, cnt_ham)
    print(f"F1-метрика со сглаживанием: {test_bayes_f1(words, test_dataset)}")
"""