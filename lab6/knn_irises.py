# Структура файла: ID,      Длина чашелистика,      Ширина чашелистика,     Длина лепестка,     Ширина лепестка,    Вид ириса
# Структура файла: ID (0),  SepalLengthCm (1),      SepalWidthCm (2),       PetalLengthCm (3),  PetalWidthCm (4),    Species (5)

# Виды ирисов в файле: Iris-setosa, Iris-versicolor, Iris-virginica

from lab6.parseCSVToDataset import parseCSV_Irises
from lab6.support_methods import find_best_k, test_knn_dataset
from random import shuffle
from dsmltf import knn_classify, principal_components, genser, train_test_split

def solve_irises():

    # Получаем датасет
    dataset = parseCSV_Irises("C:/Users/Дарья/Documents/Университет/ИАД/DataMiningDecisions/lab6/datasets/Iris.csv")

    # Перемешиваем датасет
    shuffle(dataset)

    # Разделяем данные на признаки и метки для train_test_split()
    dataset_data = [i[0] for i in dataset]
    dataset_labels = [i[1] for i in dataset]

    # Делим натренировочную и тестовую выборку
    train_data, test_data, train_labels, test_labels = train_test_split(dataset_data, dataset_labels, 0.33)

                            ##### РАБОТАЕМ С ТРЕНИРОВОЧНОЙ ВЫБОРКОЙ #####
    # Форматируем тестовую выборку в 4-мерный датасет
    dataset_train = [(data_i, label_i) for data_i, label_i in zip(train_data, train_labels)]

    # Находим лучшее k
    best_k = find_best_k(dataset_train, 20)
    print(f"При лучшем k = {best_k},")

                            ##### РАБОТАЕМ С ТЕСТОВОЙ ВЫБОРКОЙ ######
    # Снижаем размерность датасета до 2 признаков методом PCA и заново форматируем в датасет
    new_dataset_pca = principal_components(test_data, 2)
    dataset_pca = [(data_i, label_i) for data_i, label_i in zip(new_dataset_pca, test_labels)]

    # Снижаем размерность до 2 признаков методом обобщённой сериализации и заново форматируем в датасет
    new_dataset_gs, _ = genser(test_data, 2)
    dataset_gs = [(data_i, label_i) for data_i, label_i in zip(new_dataset_gs, test_labels)]

    # Форматируем 4-мерную тестовую выборку в датасет
    dataset_source_test = [(data_i, label_i) for data_i, label_i in zip(test_data, test_labels)]

    # Вычисляем соотношения (количество удачных предсказаний, общее их количество)
    correct_prediction_src, len_src = test_knn_dataset(dataset_source_test, best_k)
    correct_prediction_pca, len_pca = test_knn_dataset(dataset_pca, best_k)
    correct_prediction_gs, len_gs = test_knn_dataset(dataset_gs, best_k)

    # Находим процентрные соотношения
    percent_src = round(correct_prediction_src / len_src, 4) * 100
    percent_pca = round(correct_prediction_pca / len_pca, 4) * 100
    percent_gs = round(correct_prediction_gs / len_gs, 4) * 100

    # Выводим результаты
    print(f"Метод k ближайших соседей на 4-мерной выборке: {correct_prediction_src} / {len_src} ({percent_src}%), \n"
          f"Метод k ближайших соседей на 2-мерной выборке (метод PCA): {correct_prediction_pca} / {len_pca} ({percent_pca}%), \n"
          f"Метод k ближайших соседей на 2-мерной выборке (метод обобщённой сериализации): {correct_prediction_gs} / {len_gs}  ({percent_gs}%), \n")
