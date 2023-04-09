import numpy as np

def move(d):
    data = d.copy()
    new_data = np.zeros((data.shape[0] + 1, data.shape[1] + 1))
    for i, j in np.ndindex(data.shape):
        if data[i][j] == 1:
            new_data[i][j] = data[i][j]
        elif data[i][j] == 2:
            new_data[i+1][j+1] = data[i][j]
        elif data[i][j] == 3:
            new_data[i][j+1] = data[i][j]
        elif data[i][j] == 4:
            new_data[i+1][j] = data[i][j]
    return new_data

def fill(d):
    data = d.copy()
    diamant = np.zeros(((data.shape[0] - 1) * 2, (data.shape[0] - 1) * 2))
    for i, j in np.ndindex(data.shape):
        diamant[data.shape[1] - 1 + i - j][i + j] = data[i][j]
        if data[i][j] == 1:
            diamant[data.shape[1] + i - j][i + j] = data[i][j]
        elif data[i][j] == 2:
            diamant[data.shape[1] - 2 + i - j][i + j] = data[i][j]
        elif data[i][j] == 3:
            diamant[data.shape[1] - 1 + i - j][i + j + 1] = data[i][j]
        elif data[i][j] == 4:
            diamant[data.shape[1] - 1 + i - j][i + j - 1] = data[i][j]
    return diamant


def check(d):
    data = d.copy()
    for i in range(data.shape[0] - 1):
        for j in range(data.shape[1] - 1):
            if data[i][j] == 2 and data[i][j+1] == 1:
                data[i][j], data[i][j+1] = 0, 0

        for j in range(1, data.shape[1]):
            if data[i][j] == 4 and data[i][j-1] == 3:
                data[i][j], data[i][j-1] = 0, 0
    return data


def create(d):
    data = d.copy()
    for i, j in np.ndindex(data.shape):
        if data[i][j] == 0:
            if np.random.random() < 0.5:
                data[i][j], data[i+1][j] = 3, 4
            else:
                data[i][j], data[i+1][j] = 1, 2
    return data