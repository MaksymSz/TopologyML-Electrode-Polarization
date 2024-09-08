from computing.core import discretize
from computing.transformations import transform_pairs
from numba import njit


@njit
def make_persistent_image(pairs, resolution):
    _transformed_pairs = transform_pairs(pairs)
    return discretize(_transformed_pairs, resolution)
