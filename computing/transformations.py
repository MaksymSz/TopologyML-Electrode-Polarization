import numpy as np
from numba import njit, prange


@njit(parallel=True)
def rotate_pairs(pairs):
    for i in prange(pairs.shape[0]):
        pairs[i, 1] = pairs[i, 1] - pairs[i, 0]

    return pairs


@njit
def scale_pairs(pairs):
    min_birth = np.min(pairs[:, 0])
    min_death = np.min(pairs[:, 1])

    pairs[:, 0] -= min_birth
    pairs[:, 0] /= np.max(pairs[:, 0])

    pairs[:, 1] -= min_death
    pairs[:, 1] /= np.max(pairs[:, 1])

    return pairs


@njit
def transform_pairs(pairs):
    return scale_pairs(rotate_pairs(pairs))