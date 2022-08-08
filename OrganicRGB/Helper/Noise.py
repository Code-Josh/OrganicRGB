import numpy as np
import opensimplex.internals as simplex_i
from numba import njit, prange


simplex4dNoise = simplex_i._noise4
init = simplex_i._init


@njit(fastmath=True, cache=True)
def get_2DNoiseDeviceMatrix(coordinates: np.ndarray,
                            t: float,
                            num_led: int, feature_size: float, color_channels: np.ndarray['N,3', np.dtype[np.float64]],
                            perm: np.ndarray['256', np.dtype[np.int64]],
                            beat_power: float = 0.0, device_id: int = 0) -> np.ndarray['N', np.dtype[np.float64]]:
    NoiseList = np.zeros((num_led, 3), dtype=np.float64)
    for led in coordinates:
        x, y, z, led_id = led[0], led[1], led[2], led[3]
        NoiseList[led_id] = get_NoisePixel(x, y, z, t, feature_size, color_channels, perm, beat_power=beat_power,
                                   device_id=device_id)

    return NoiseList


@njit(fastmath=True, cache=True)
def get_NoiseMatrix(width: float, height: float, subdiv: float, t: float, feature_size: float,
                    color_channels: np.ndarray['N,3', np.dtype[np.float64]],
                    perm: np.ndarray['256', np.dtype[np.int64]],
                    beat_power: float = 0.0, device_id: int = 0) -> np.ndarray['N,N,3', np.dtype[np.float64]]:
    image = np.zeros((width // subdiv, height // subdiv, 3), dtype=np.float64)
    for a in prange(0, width // subdiv):
        for b in prange(0, height // subdiv):
            image[a][b] = get_NoisePixel(a * subdiv, b * subdiv, 0, t, feature_size, color_channels, perm,
                                         beat_power=beat_power, device_id=device_id)
    return image


@njit(fastmath=True, cache=True)
def get_NoisePixel(h: float, w: float, d: float, t: float, feature_size: float,
                   color_channels: np.ndarray['N,3', np.dtype[np.float64]], perm: np.ndarray['256', np.dtype[np.int64]],
                   beat_power: float = 0.0, device_id: int = 0) -> np.ndarray['3', np.dtype[np.float64]]:
    color = np.zeros(3, np.float64)
    index = 0
    for c in color_channels[:-1]:
        factor = (simplex4dNoise(h / feature_size, w / feature_size, d / feature_size,
                                 t + 10000 * index + device_id * 1000000, perm) + 1) / 2
        color += c * factor
        index += 1
    if beat_power > 0.0:
        device_id += 10
        index = 0
        factor = (simplex4dNoise(h / feature_size, w / feature_size, d / feature_size,
                                 t + 10000 * index + device_id * 1000000, perm) + 1) / 2
        factor *= beat_power
        factor = pow(factor, 0.75)
        color = color * (1 - factor) + color_channels[-1] * factor
    return color
