import csv
from matplotlib import pyplot


def parseCSV(path):
    """
    Вытаскивает данные из CSV-файла про ирисы и форматирует их
    :param path: Путь к файлу
    :return: Список точек для кластеризации
    """
    with open(path, 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        dataset = []

        for line in reader:
            if line[0] == "Id": continue

            dataset.append((float(line[3]), float(line[4])))

        return dataset


def make_plot_clusters(clusters: dict):
    """
    Строит график кластеров
    :param clusters: Список кластеров
    """
    twoD_result = {}

    for k in range(len(clusters)):
        twoD_result[k] = {}
        twoD_result[k]['x'] = [point[0] for point in clusters[k]]
        twoD_result[k]['y'] = [point[1] for point in clusters[k]]

        # Рисуем точки, распределённые по кластерам, с разными цветами
        pyplot.scatter(twoD_result[k]['x'], twoD_result[k]['y'], marker='o', label=f"Кластер {k + 1}")

    pyplot.title(f'k = {len(clusters)}')
    pyplot.legend()
    pyplot.show()

#-----------------------------------------------------------------------------------------------------------------------
