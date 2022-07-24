from openrgb import orgb
from .Keyboard import roccat_vulcan_120_aimo
from OrganicRGB.DeviceTypes import *

__devices__ = {
    'Roccat Vulcan 120 Aimo': roccat_vulcan_120_aimo.main()
}

class Keyboard:
    def __init__(self, rgb_device: orgb.Device):
        self.name = rgb_device.name
        self.settings = None
        self.noise_id = 1
        self.rgb = rgb_device
        if self.name in __devices__:
            self.settings = __devices__[self.name]
        else:
            print(f'{self.name} is not supported')