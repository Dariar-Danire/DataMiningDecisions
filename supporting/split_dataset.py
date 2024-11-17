from dsmltf import train_test_split


def train_test_dataset_split(dataset, p=1/3):
    x = [i[0] for i in dataset]
    y = [i[1] for i in dataset]

    train_data, test_data, train_res, test_res = train_test_split(x, y, p)

    train_dataset = [(x_i, y_i) for x_i, y_i in zip(train_data, train_res)]
    test_dataset = [(x_i, y_i) for x_i, y_i in zip(test_data, test_res)]

    return train_dataset, test_dataset
