import math

import numpy as np
from numba import njit, jit, prange
from openrgb.utils import RGBColor

multiplication_vector = np.array((0.2989, 0.5870, 0.114), dtype=np.float64)


def np_to_RGB(nparray: np.ndarray['N,3', np.dtype[np.uint8]]) -> list[RGBColor]:
    openrgb_values = []
    for value in nparray:
        rgb = RGBColor(value[0], value[1], value[2])
        openrgb_values.append(rgb)
    return openrgb_values


@njit(fastmath=True, cache=True)
def m_correct_gamma(matrix: np.ndarray['N,N,3', np.dtype[np.float64]], linear_correction: float) -> np.ndarray[
    'N,N,3', np.dtype[np.float64]]:
    return matrix * linear_correction


v_correct_gamma = m_correct_gamma


@njit(fastmath=True, cache=True)
def v_linear_to_srgb(vector: np.ndarray['N,3', np.dtype[np.float64]]) -> np.ndarray[
    'N,3', np.dtype[np.float64]]:
    for a in prange(len(vector)):
        for b in prange(3):
            if vector[a][b] <= 0.0031308:
                vector[a][b] *= 12.92
            else:
                vector[a][b] = 1.055 * pow(vector[a][b], 1 / 2.4) - 0.055
    return vector


@njit(fastmath=True, cache=True)
def m_linear_to_srgb(matrix: np.ndarray['N,N,3', np.dtype[np.float64]]) -> np.ndarray[
    'N,N,3', np.dtype[np.float64]]:
    for a in prange(len(matrix)):
        for b in prange(len(matrix[0])):
            for c in prange(3):
                if matrix[a][b][c] <= 0.0031308:
                    matrix[a][b][c] *= 12.92
                else:
                    matrix[a][b][c] = 1.055 * pow(matrix[a][b][c], 1 / 2.4) - 0.055
    return matrix


@njit(cache=True)
def saturate(color, s_factor, v_factor):
    y = math.sqrt(0.2989 * color[0] ** 2 + 0.5870 * color[1] ** 2 + 0.1140 * color[2] ** 2)
    color = (-y * s_factor + color * (1 + s_factor)) * v_factor
    return color


@jit(fastmath=True, cache=True)
def v_saturate(vector: np.ndarray['N,3', np.dtype[np.float64]], s_factor: float, v_factor: float) -> np.ndarray[
    'N,3', np.dtype[np.float64]]:
    sum_v = np.sum((vector ** 2) * multiplication_vector, axis=1)

    new_shape = (sum_v.shape[0], 1)
    sum_v = np.reshape(sum_v, new_shape)
    v_y = np.sqrt(sum_v)
    n_vector = (-v_y * s_factor + vector * (1 + s_factor)) * v_factor
    return n_vector


@jit(fastmath=True, cache=True)
def m_saturate(matrix: np.ndarray['N,N,3', np.dtype[np.float64]], s_factor: float, v_factor: float) -> np.ndarray[
    'N,N,3', np.dtype[np.float64]]:
    sum_m = np.sum((matrix ** 2) * multiplication_vector, axis=2)
    new_shape = (sum_m.shape[0], sum_m.shape[1], 1)
    sum_m = np.reshape(sum_m, new_shape)
    m_y = np.sqrt(sum_m)
    n_matrix = (-m_y * s_factor + matrix * (1 + s_factor)) * v_factor
    return n_matrix


@njit(cache=True)
def normalize(color):
    for i in range(0, 3):
        if color[i] > 1.0:
            color[i] = 1.0
        elif color[i] < 0.0:
            color[i] = 0.0
    color = np.floor(color * 255).astype('uint8')
    return color


@njit(fastmath=True, cache=True)
def m_normalize(matrix: np.ndarray['N,N,3', np.dtype[np.float64]]) -> np.ndarray['N,N,3', np.dtype[np.uint8]]:
    matrix = np.clip(matrix, 0, 1)
    color = np.floor(matrix * 255 + 0.5).astype('uint8')
    return color


v_normalize = m_normalize
