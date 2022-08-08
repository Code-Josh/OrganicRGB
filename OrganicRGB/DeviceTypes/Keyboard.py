import numpy as np
from openrgb import OpenRGBClient
from openrgb.utils import DeviceType


class german_keys:
    num_leds = 0

    def __init__(self):
        keyboard = OpenRGBClient().get_devices_by_type(DeviceType.KEYBOARD)[0]
        self.keys = keyboard.leds
        self.key_data = np.zeros(len(self.keys),
                                 dtype=[('x', np.float64), ('y', np.float64), ('z', np.float64), ('id', np.uint16)])
        self.num_leds = len(self.keys)

        index = 0
        for key_id, key in enumerate(self.keys):
            if key.name != 'Unused':
                self.key_data[index] = (0, 0, 0, key_id)
                index += 1
        self.key_data = self.key_data[:index]

    def K_Escape(self, x=0, y=0):
        key_id = 0
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Circumflex(self, x=0, y=0):
        key_id = 1
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Tab(self, x=0, y=0):
        key_id = 2
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Caps_Lock(self, x=0, y=0):
        key_id = 3
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Left_Shift(self, x=0, y=0):
        key_id = 4
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Left_Control(self, x=0, y=0):
        key_id = 5
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_1(self, x=0, y=0):
        key_id = 6
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Q(self, x=0, y=0):
        key_id = 7
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_A(self, x=0, y=0):
        key_id = 8
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Lessthan(self, x=0, y=0):
        key_id = 9
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Left_Windows(self, x=0, y=0):
        key_id = 10
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_F1(self, x=0, y=0):
        key_id = 11
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_2(self, x=0, y=0):
        key_id = 12
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_W(self, x=0, y=0):
        key_id = 13
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_S(self, x=0, y=0):
        key_id = 14
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Y(self, x=0, y=0):
        key_id = 15
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Left_Alt(self, x=0, y=0):
        key_id = 16
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_F2(self, x=0, y=0):
        key_id = 17
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_3(self, x=0, y=0):
        key_id = 18
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_E(self, x=0, y=0):
        key_id = 19
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_D(self, x=0, y=0):
        key_id = 20
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_X(self, x=0, y=0):
        key_id = 21
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_F3(self, x=0, y=0):
        key_id = 22
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_4(self, x=0, y=0):
        key_id = 23
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_R(self, x=0, y=0):
        key_id = 24
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_F(self, x=0, y=0):
        key_id = 25
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_C(self, x=0, y=0):
        key_id = 26
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_F4(self, x=0, y=0):
        key_id = 27
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_5(self, x=0, y=0):
        key_id = 28
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_T(self, x=0, y=0):
        key_id = 29
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_G(self, x=0, y=0):
        key_id = 30
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_V(self, x=0, y=0):
        key_id = 31
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_6(self, x=0, y=0):
        key_id = 32
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Z(self, x=0, y=0):
        key_id = 33
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_H(self, x=0, y=0):
        key_id = 34
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_B(self, x=0, y=0):
        key_id = 35
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Space(self, x=0, y=0):
        key_id = 36
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_F5(self, x=0, y=0):
        key_id = 37
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_7(self, x=0, y=0):
        key_id = 38
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_U(self, x=0, y=0):
        key_id = 39
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_J(self, x=0, y=0):
        key_id = 40
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_N(self, x=0, y=0):
        key_id = 41
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_F6(self, x=0, y=0):
        key_id = 42
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_8(self, x=0, y=0):
        key_id = 43
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_I(self, x=0, y=0):
        key_id = 44
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_K(self, x=0, y=0):
        key_id = 45
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_M(self, x=0, y=0):
        key_id = 46
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_F7(self, x=0, y=0):
        key_id = 47
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_9(self, x=0, y=0):
        key_id = 48
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_O(self, x=0, y=0):
        key_id = 49
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_L(self, x=0, y=0):
        key_id = 50
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Comma(self, x=0, y=0):
        key_id = 51
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_F8(self, x=0, y=0):
        key_id = 52
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_0(self, x=0, y=0):
        key_id = 53
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_P(self, x=0, y=0):
        key_id = 54
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_OE(self, x=0, y=0):
        key_id = 55
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Dot(self, x=0, y=0):
        key_id = 56
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Right_Alt(self, x=0, y=0):
        key_id = 57
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Sharp_S(self, x=0, y=0):
        key_id = 58
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_UE(self, x=0, y=0):
        key_id = 59
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_AE(self, x=0, y=0):
        key_id = 60
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Minus(self, x=0, y=0):
        key_id = 61
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Right_Fn(self, x=0, y=0):
        key_id = 62
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_F9(self, x=0, y=0):
        key_id = 63
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Acute_Accent(self, x=0, y=0):
        key_id = 64
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Plus(self, x=0, y=0):
        key_id = 65
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Right_Shift(self, x=0, y=0):
        key_id = 66
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Menu(self, x=0, y=0):
        key_id = 67
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_F10(self, x=0, y=0):
        key_id = 68
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_F11(self, x=0, y=0):
        key_id = 69
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_F12(self, x=0, y=0):
        key_id = 70
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Backspace(self, x=0, y=0):
        key_id = 71
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Enter(self, x=0, y=0):
        key_id = 72
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Right_Control(self, x=0, y=0):
        key_id = 73
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Hashtag(self, x=0, y=0):
        key_id = 74
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Print_Screen(self, x=0, y=0):
        key_id = 75
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Insert(self, x=0, y=0):
        key_id = 76
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Delete(self, x=0, y=0):
        key_id = 77
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Left_Arrow(self, x=0, y=0):
        key_id = 78
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Scroll_Lock(self, x=0, y=0):
        key_id = 79
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Home(self, x=0, y=0):
        key_id = 80
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_End(self, x=0, y=0):
        key_id = 81
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Up_Arrow(self, x=0, y=0):
        key_id = 82
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Down_Arrow(self, x=0, y=0):
        key_id = 83
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Pause_Break(self, x=0, y=0):
        key_id = 84
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Page_Up(self, x=0, y=0):
        key_id = 85
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Page_Down(self, x=0, y=0):
        key_id = 86
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Right_Arrow(self, x=0, y=0):
        key_id = 87
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Num_Lock(self, x=0, y=0):
        key_id = 88
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_7(self, x=0, y=0):
        key_id = 89
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_4(self, x=0, y=0):
        key_id = 90
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_1(self, x=0, y=0):
        key_id = 91
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_0(self, x=0, y=0):
        key_id = 92
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_Slash(self, x=0, y=0):
        key_id = 93
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_8(self, x=0, y=0):
        key_id = 94
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_5(self, x=0, y=0):
        key_id = 95
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_2(self, x=0, y=0):
        key_id = 96
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_Star(self, x=0, y=0):
        key_id = 97
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_9(self, x=0, y=0):
        key_id = 98
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_6(self, x=0, y=0):
        key_id = 99
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_3(self, x=0, y=0):
        key_id = 100
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_Comma(self, x=0, y=0):
        key_id = 101
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_Minus(self, x=0, y=0):
        key_id = 102
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_Plus(self, x=0, y=0):
        key_id = 103
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0

    def K_Number_Pad_Enter(self, x=0, y=0):
        key_id = 104
        self.key_data[key_id]['x'] = x
        self.key_data[key_id]['y'] = y
        self.key_data[key_id]['z'] = 0.0
