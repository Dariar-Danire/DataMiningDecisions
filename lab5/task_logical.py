import random
from functools import partial
from dsmltf import scale, log_likelyhood, train_test_split, gradient_descent, negate, sigmoid, dot, f1_score

"""
Выберу ли я книгу из художественной литературы для прочтения? Параметры выбора:
1) Рейтинг: 0-5☆
2) Сюжет книги: шаблонный (0), оригинальный (1)
3) Жанр: драма (0), ужасы (1), фентези (2), фантастика (3)
4) Автор: не нравится (0), неизвестен (1), нравится (2)
5) Стиль повествования автора: нудный (0), захватывающий внимание (1)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------7) Грамотность автора: больно читать (0), хорошо или нормально (1)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------5) Краткое писание: посредственное (0), интригующее (1)

Результаты: ищу другую книгу (0), читаю эту (1)

Пример элемента выборки X: [5, 1, 5, 2, 0, 1, 0] и соответствующий ему результат выборки y: [0].

Если объединить в одно, получится так: 
[5, 1, 5, 2, 0, 1, 0, 0]
"""

# data = [rating, books_plot, genre, author, narrative_style, i_read]
def solve(data: list):
    for i in range(len(data)):
        print(f"{i + 1}. Рейтинг: {data[i][0]}, Сюжет: {data[i][1]}, Автор: {data[i][2]}, Стиль письма: {data[i][3]}, Жанр: {data[i][4]}, Результат: {data[i][5]}")
    print("\n")

    k = len(data[0]) - 1  # Количество критериев

    # Готовим данные в классической для регрессии форме
    x = [[1] + r[:k] for r in data]     # Список для параметров (1 - это коэфициент перед alpha): alpha + beta_0 * a + beta_1 * b + beta_2 * c + beta_3 * epsilon
    y = [r[k] for r in data]            # Список для результатов (статус): y

    # Прошкалируем данные
    x_scale = scale(x)

    # Нужно разделить выборку на обучающую и тестовую
    random.seed(0)
    x_train, x_test, y_train, y_test = train_test_split(x_scale, y, 0.33) # Почему вероятность 0.33 и что за вероятность?

    # Максимизируем функцию правдоподобия на обучающей выборке
    fn = partial(log_likelyhood, x_train, y_train)

    # Устанавливаем отправную точку
    beta_0 = [random.random() for _ in range(6)]

    # Максимизиуем fn гадиентным спуском
    beta_hat = gradient_descent(negate(fn), beta_0)
    print(beta_hat)

    true_positives, true_negatives, false_positives, false_negatives = 0, 0, 0, 0
    for x_i, y_i in zip(x_test, y_test):
        predict = sigmoid(dot(beta_hat[0], x_i))
        if y_i == 1 and predict >= 0.5:
            true_positives += 1
        elif y_i == 1:
            false_negatives += 1
        elif predict >= 0.5:
            false_positives += 1
        else:
            true_negatives += 1

    f1_scr = f1_score(true_positives, false_positives, false_negatives)

    print(f"F1-метрика: {f1_scr}")
