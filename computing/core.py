import numpy as np
from numba import njit, prange
from computing.integrate import glqaud

COV = 2 * 0.05 ** 2
FACTOR = 2 * np.pi * 0.05 ** 2

# constants from Kusano paper
C = 500
P = 50


@njit
def make_grid(res):
    _grid = np.repeat(np.linspace(0, 1, res + 1), res + 1).reshape(res + 1, res + 1)
    return _grid.T, _grid


@njit
def multivariate_normal_pdf(x, y, z):
    """
        Function to compute the PDF of a multivariate normal distribution.

        In this case I use the assumption that covariance between birth and persistence equals 0.05
        """
    diff_x = x - z[0]
    diff_y = y - z[1]
    exponent = (diff_x ** 2 + diff_y ** 2) / COV
    pdf_value = np.exp(-0.5 * exponent) / FACTOR
    return z[2] * np.arctan(C * z[1] ** P) * pdf_value


@njit(parallel=False)
def persistent_surface(x, y, pairs):
    """
    Function to compute the persistent surface.
    .. math::
        \\rho _B(z) = \\sum_{u \\in T(B)} w(u)\\phi_\\mu(z)
    """
    rho = 0
    for i in range(pairs.shape[0]):
        rho += multivariate_normal_pdf(x, y, pairs[i])
    return rho


@njit(parallel=True)
def discretize(pairs, res):
    """
    Function to discretize the persistent surface to :math:`MxM` matrix according to:
    .. math::
        PI(D)_{i,j} := \\int_{P_{i,j}} \\rho{D}(u) du
    """
    pi_ = np.empty((res * res), dtype=np.float64)

    x_grid, y_grid = make_grid(res)
    for idx in prange(res * res):
        i = idx // res
        j = idx % res
        r = glqaud(persistent_surface, x_grid[i, j], x_grid[i, j + 1], y_grid[i, j], y_grid[i + 1, j],
                   pairs=pairs)
        pi_[idx] = r

    return pi_
