import numpy as np
import math

def saturate(color, s_factor, v_factor):
    y = math.sqrt(0.2989 * color[0]**2 + 0.5870 * color[1]**2 + 0.1140 * color[2]**2)
    color = (-y * s_factor + color * (1 + s_factor))*v_factor
    return color

def normalize(color):
    for i in range(0, 3):
        if color[i] > 1.0:
            color[i] = 1.0
        elif color[i] < 0.0:
            color[i] = 0.0
    color = np.floor(color*255).astype('uint8')
    return color