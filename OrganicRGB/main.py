import numpy as np
import opensimplex as simplex
from openrgb import OpenRGBClient
from openrgb.utils import DeviceType
import time
from math import pow, sqrt
import pygame
import OrganicRGB.Devices as ORGBDevices
from OrganicRGB.Helper import Sound, Color, Noise
from numba import jit

subdiv = 8

multiplication_vector = np.array((0.2989, 0.5870, 0.114), dtype=np.float64)

class main:
    case_height = 0 #mm
    case_width = 0 #mm
    case_depth = 0 #mm

    color_channels = []
    feature_size = 200

    start_time = 0
    music = {'beat': False}

    def __init__(self, color_settings, noise_settings, music=None):
        self.loop = True
        self.case_height = None
        self.case_width = None
        self.case_depth = None
        self.feature_size = 100
        self.speed = 100
        self.seed = 100

        if 'speed' in noise_settings:
            self.speed = noise_settings['speed']
        if 'feature_size' in noise_settings:
            self.feature_size = noise_settings['feature_size']
        if 'seed' in noise_settings:
            self.seed = noise_settings['seed']

        start = 0.0
        real = np.zeros(3, dtype=np.float64)

        for c in color_settings['colorpalette']:
            c = np.array(c, dtype=np.float64) / 255
            start += sqrt(np.sum(c ** 2 * multiplication_vector))
            real += c
            self.color_channels.append(c)

        start = start / len(self.color_channels)
        real = sqrt(np.sum(((real ** 2) / len(self.color_channels) * multiplication_vector)))
        self.gamma_correction = (start / real) ** 2
        print('Correction', self.gamma_correction)

        if music != None:
            self.music = music
            self.color_channels.append(np.array(self.music['color'], dtype=np.uint8) / 255)
        self.color_channels = np.array(self.color_channels, dtype=np.float64)

        self.saturation = color_settings['saturation']
        self.color_value = color_settings['value']
        self.start_time = time.time()
        self.rgb_ids = []
        simplex.seed(self.seed)
        self.cli = OpenRGBClient()
        self.devices = {}
        self.search_devices()
        self.beat_helper = Sound.helper()

    def set_case(self, h, w, d):
        self.case_height = h
        self.case_width = w
        self.case_depth = d

    def get_Devices(self):
        status = []
        for device in self.devices.keys():
            status.append(self.devices[device][1])
        return [list(self.devices.keys()), status]

    def activate_Device(self, name):
        self.devices[name][1] = True

    def deactivate_Device(self, name):
        self.devices[name][1] = False

    def search_devices(self):
        #keyboards
        keyboards = self.cli.get_devices_by_type(DeviceType.KEYBOARD)
        if len(keyboards) == 1:
            self.devices['Keyboard'] = [ORGBDevices.Keyboard(keyboards[0]), False]
            self.rgb_ids.append(1)
            keyboards[0].clear()

    """def mainloop(self):
        arith_time, y = 0, 0.5
        index = 0
        status_update = 100
        device, on = self.devices['Keyboard']
        key_array = np.zeros((len(device.settings.keys.data.items()), 3), dtype=np.uint16)
        index = 0
        for item in device.settings.keys.data.items():
            key = item[1]
            key_array[index][0] = key['x']
            key_array[index][1] = key['y']
            key_array[index][2] = key['id']
            index += 1

        while self.loop:
            start_time = time.time_ns()
            t = self.speed * (time.time() - self.start_time) / 100
            beat_power = 0
            if self.music['beat']:
                self.beat_helper.mainloop()
                beat_power, fft = self.beat_helper.get_last_data()
            nprgb = self.update_keyboard(t, key_array, device.settings.keys.num_leds + 1, beat_power=beat_power)
            openrgb_values = self.np_to_RGB(nprgb)
            #print(openrgb_values[0].red)
            device.rgb.set_colors(self.np_to_RGB(nprgb))
            device.rgb.update()
            arith_time = (time.time_ns() - start_time) * y + arith_time * (1-y)
            index += 1
            if index % status_update == 0:
                print(1000000000/arith_time)"""

    def update_keyboard(self, t, perm, beat_power=0):
        device, on = self.devices['Keyboard']
        key_data = device.settings.keys.key_data
        num_leds = device.settings.keys.num_leds
        RGBVector = Noise.get_2DNoiseDeviceMatrix(key_data, t, num_leds, self.feature_size, self.color_channels, perm, beat_power=beat_power)
        RGBVector = Color.v_saturate(RGBVector, self.saturation, self.color_value)
        RGBVector = Color.v_correct_gamma(RGBVector, self.gamma_correction)
        RGBVector = Color.v_normalize(RGBVector)
        OpenRGBVector = Color.np_to_RGB(RGBVector)

        device.rgb.set_colors(OpenRGBVector)
        device.rgb.update()

    def update_Devices(self, t, perm, beat_power=0):
        for dev in self.devices:
            if dev == 'Keyboard':
                if self.devices[dev][1]:
                    self.update_keyboard(t, perm, beat_power=beat_power)

    @jit(forceobj=True)
    def show2D(self, height, width):
        pygame.init()
        self.display = pygame.display.set_mode((width * 2, height * 2))
        pygame.display.set_caption('2D RGB Preview')

        perm = Noise.init(3)[0]

        running = True
        while running:
            start_time = time.time()
            t = self.speed * (time.time() - self.start_time) / 100
            beat_power = 0
            if self.music['beat']:
                self.beat_helper.mainloop()
                beat_power, fft = self.beat_helper.get_last_data()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            image = Noise.get_NoiseMatrix(width, height, subdiv, t, self.feature_size, self.color_channels, perm)
            image = Color.m_saturate(image, self.saturation, self.color_value)
            image = Color.m_correct_gamma(image, self.gamma_correction)
            image = Color.m_linear_to_srgb(image)
            image = Color.m_normalize(image)

            self.update_Devices(t, perm, beat_power=beat_power)
            surf = pygame.surfarray.make_surface(image)
            surf = pygame.transform.scale(surf, (width * 2, height * 2))
            self.display.blit(surf, (0, 0))
            pygame.display.update()
            delta_time = time.time() - start_time
            print(1/delta_time)
        pygame.quit()
