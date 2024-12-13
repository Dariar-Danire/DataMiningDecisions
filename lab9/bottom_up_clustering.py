from dsmltf import distance


def generate_clusters(base_cluster, num_clusters):
    """
    Разделяет base_cluster на num_clusters кластеров
    :param base_cluster: Базовый кластер
    :param num_clusters: Число итоговых кластеров
    :return: Итоговые кластеры
    """
    clusters = [base_cluster]
    while len(clusters) < num_clusters:
        next_cluster = min(clusters, key=get_merge_order)
        clusters = [c for c in clusters if c != next_cluster]
        clusters.extend(get_children(next_cluster))
    return clusters


def bottom_up_cluster(inps, distance_agg=min):
    """
    Реализация алгоритма восходящей кластеризации
    :param inps: Список исходных точек
    :param distance_agg: Целевая функция
    :return: Базовый кластер
    """

    # Определяем len(inps) кластеров
    clusters = [(inp,) for inp in inps]

    # Пересчитываем кластеры, до тех пор, пока у нас не останется хотя бы 2 кластера
    while len(clusters) > 1:
        # Находим 2 ближайших кластера
        c1, c2 = min([(cluster1, cluster2)
                      for i, cluster1 in enumerate(clusters)
                      for cluster2 in clusters[:i]],
                     key=lambda x: cluster_distance(*x, distance_agg))

        # Перезаписываем все кластеры, кроме c1 и c2
        clusters = [c for c in clusters if c != c1 and c != c2]

        # Записываем объединённый кластер
        merged_cluster = (len(clusters), [c1, c2])
        clusters.append(merged_cluster)

    return clusters[0]


def cluster_distance(cluster1, cluster2, distance_agg=min):
    """
    Вычисляет расстояние между кластерами
    :param cluster1: Первый кластер
    :param cluster2: Второй кластер
    :param distance_agg: Целевая функция (по умолчанию минимизируем расстояние)
    """
    values1 = list(get_values(cluster1))
    values2 = list(get_values(cluster2))
    return distance_agg([distance(list(inp1), list(inp2)) for inp1 in values1 for inp2 in values2])


def get_values(cluster):
    """
    Выдаёт значения кластера
    :param cluster: Кластер
    """
    if is_leaf(cluster):
        return [cluster[0]]
    else:
        return [val for child in get_children(cluster)
                for val in get_values(child)]


def get_children(cluster):
    """
    Выдаёт дочерний элемент кластера
    :param cluster: Кластер
    """
    if is_leaf(cluster):
        raise TypeError('Одноточечный кластер не имеет дочерних кластеров')
    else:
        return cluster[1]


def get_merge_order(cluster):
    """
    Выдаёт порядковый номер объединения кластеров
    :param cluster: Кластер
    """
    if is_leaf(cluster):
        return float('inf')
    else:
        return cluster[0]


def is_leaf(cluster):
    """
    Определяет одноточечный ли кластер
    :param cluster: Кластер
    :return: True - кластер одноточечный, False - кластер не одноточечный.
    """
    return len(cluster) == 1
