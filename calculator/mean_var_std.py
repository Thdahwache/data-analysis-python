import numpy as np


def calculate(list):
    # generate error if list is smaller than 9 items.
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        # convert list to array
        mtx = np.array(list).reshape(3, 3)
        # mean
        mean = [(np.mean(mtx, axis=0)).tolist(), (np.mean(mtx, axis=1)).tolist(),
                (np.mean(mtx.flatten()))]
        # variance
        var = [(np.var(mtx, axis=0)).tolist(), (np.var(mtx, axis=1)).tolist(),
               (np.var(mtx.flatten()))]
        # standard deviation
        std = [(np.std(mtx, axis=0)).tolist(), (np.std(mtx, axis=1)).tolist(),
               (np.std(mtx.flatten()))]
        # maximum
        max = [(np.max(mtx, axis=0)).tolist(), (np.max(mtx, axis=1)).tolist(),
               (np.max(mtx.flatten()))]
        # minimum
        min = [(np.min(mtx, axis=0)).tolist(), (np.min(mtx, axis=1)).tolist(),
               (np.min(mtx.flatten()))]
        # sum
        sum = [(np.sum(mtx, axis=0)).tolist(), (np.sum(mtx, axis=1)).tolist(),
               (np.sum(mtx.flatten()))]

        calculations = {
            "mean": mean,
            "variance": var,
            "standard deviation": std,
            "max": max,
            "min": min,
            "sum": sum,
        }
    return calculations
