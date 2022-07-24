import numpy as np
import opensimplex as simplex
from openrgb import OpenRGBClient
from openrgb.utils import DeviceType, RGBColor
import time
from math import pow
import pygame
import OrganicRGB.Devices as ORGBDevices
from OrganicRGB.Helper import Sound, Color

subdiv = 8

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
        if music != None:
            self.music = music
            self.music['color'] = beat_color = np.array(self.music['color'], dtype='double') / 255
        self.feature_size = 100
        self.speed = 100
        self.seed = 100

        if 'speed' in noise_settings:
            self.speed = noise_settings['speed']
        if 'feature_size' in noise_settings:
            self.feature_size = noise_settings['feature_size']
        if 'seed' in noise_settings:
            self.seed = noise_settings['seed']

        for c in color_settings['colorpalette']:
            self.color_channels.append(np.array(c, dtype='uint8') / 255)
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

    """def mainloop(self, show2D=False):
        if show2D:
            pygame.init()
            for
            while self.loop:
                t = self.speed * (time.time() - self.start_time) / 100
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.loop = False

                for a in range(0, width // subdiv):
                    for b in range(0, height // subdiv):
                        pixel = self.getBGPixel(a * subdiv, b * subdiv, 10000, t)
                        image[a][b] = pixel
                self.update_keyboard(t)
                surf = pygame.surfarray.make_surface(image)
                surf = pygame.transform.scale(surf, (width * 2, height * 2))
                self.display.blit(surf, (0, 0))
                pygame.display.update()
        else:
            while self.loop:
                t = self.speed * (time.time() - self.start_time) / 100
                self.update_keyboard(t)
                time.sleep(0.1)"""

    def update_keyboard(self, t, beat_power=0):
        device, on = self.devices['Keyboard']
        if on:
            rgb_data = []
            for i in range(0, device.settings.keys.num_leds + 1):
                rgb_data.append(RGBColor(0, 0, 0))
            for key_data in device.settings.keys.data.items():
                #key_data = rgb.keys.data[key]
                key_data = key_data[1]
                #print(key_data[])
                x = key_data['x']
                y = key_data['y']
                if x != None and y != None:
                    id = key_data['id']
                    rgb_value = self.getBGPixel(x, y, 10000, t, beat_power=beat_power) # d= 10000 cause keyboard needs own image
                    openrgb_value = RGBColor(rgb_value[0], rgb_value[1],rgb_value[2])
                    rgb_data[id] = openrgb_value
                    #device.leds[id].set_color(openrgb_value)
            device.rgb.set_colors(rgb_data)
            device.rgb.update()

    def show2D(self, height, width):
        #pygame.init()
        #self.display = pygame.display.set_mode((width * 2, height * 2))
        #pygame.display.set_caption('2D Living RGB')
        image = np.zeros((width // subdiv, height // subdiv, 3), dtype='uint8')

        running = True
        start_time = time.time()
        while running:
            start_time = time.time()
            t = self.speed * (time.time() - self.start_time) / 100
            self.beat_helper.mainloop()
            beat_power, fft = self.beat_helper.get_last_data()
            """for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for a in range(0, width // subdiv):
                for b in range(0, height // subdiv):

                    pixel = self.getBGPixel(a * subdiv, b * subdiv, 10000, t, beat_power=beat_power)
                    image[a][b] = pixel"""
            self.update_keyboard(t, beat_power=beat_power)
            #surf = pygame.surfarray.make_surface(image)
            #surf = pygame.transform.scale(surf, (width * 2, height * 2))
            #self.display.blit(surf, (0, 0))
            #pygame.display.update()
            delta_time = time.time() - start_time
            print(1/delta_time)
        #pygame.quit()

    def getBGPixel(self, h, w, d, t, beat_power=0, id=0):
        color = np.zeros(3, dtype='double')
        color = color + 1
        index = 0

        #mixing color alg
        for c in self.color_channels:
            factor = (simplex.noise4(h / self.feature_size, w / self.feature_size, d / self.feature_size, t + 10000 * index + id * 1000000) + 1) / 2
            color *= 1 - (c * factor)
            index += 1
        color = 1 - color
        if self.music['beat']:
            id += 10
            index = 0
            factor = (simplex.noise4(h / self.feature_size, w / self.feature_size, d / self.feature_size, t + 10000 * index + id * 1000000) + 1) / 2
            factor *= beat_power
            factor = pow(factor, 0.75)
            color = color*(1-factor) + self.music['color'] * factor
            #print('a', color)
        color = Color.saturate(color, self.saturation, self.color_value)
        color = Color.normalize(color)
        return color