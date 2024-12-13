from pprint import pprint
from lab9.k_means_clustering import find_best_k, clustering
from lab9.support_methods import parseCSV, make_plot_clusters
from dsmltf import scale
from lab9.rising_clastering import rising_clustering, euclidean_dist


def solve():
    # Формируем датасет
    dataset = parseCSV('C:/Users/Дарья/Documents/Университет/ИАД/DataMiningDecisions/lab9/datasets/Iris.csv')

    # Шкалируем данные
    scaled_dataset = scale(dataset)

    # Определяем лучшее k
    k = find_best_k(scaled_dataset, 8)

    # Кластеризация методом k средних
    centers_of_clusters, KMeans_clusters = clustering(scaled_dataset, k)

    print("Результат кластеризации методом k средних:")
    pprint(KMeans_clusters)
    make_plot_clusters(KMeans_clusters)

    # Кластеризация восходящим методом с помощью rising_clustering
    rising_clusters = rising_clustering(scaled_dataset, euclidean_dist,  0.8)

    print("\nРезультат кластеризации восходящим методом с помощью rising_clustering:")
    pprint(rising_clusters)
    make_plot_clusters(rising_clusters)
