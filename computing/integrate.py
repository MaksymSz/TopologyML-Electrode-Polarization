import numpy as np
from numba import njit

ABSCISSAS = np.array([-0.9061798459386640,
                      -0.5384693101056831,
                      0,
                      0.5384693101056831,
                      0.9061798459386640])
WEIGHTS = np.array([0.2369268850561891,
                    0.4786286704993665,
                    0.5688888888888889,
                    0.4786286704993665,
                    0.2369268850561891])


@njit
def glqaud(f, a_x, b_x, a_y, b_y, pairs):
    _x_gauss_scaled = ((b_x - a_x) * ABSCISSAS + b_x + a_x) / 2
    _y_gauss_scaled = ((b_y - a_y) * ABSCISSAS + b_y + a_y) / 2

    _sum = 0

    for i in range(5):
        for j in range(5):
            _sum += WEIGHTS[i] * WEIGHTS[j] * f(_x_gauss_scaled[i], _y_gauss_scaled[j], pairs)

    return _sum * (b_x - a_x) / 2 * (b_y - a_y) / 2
