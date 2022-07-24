from openrgb import OpenRGBClient
from openrgb.utils import DeviceType


class german_keys:
    data = {}
    unused_leds = []
    num_leds = 0

    def __init__(self):
        keyboard = OpenRGBClient().get_devices_by_type(DeviceType.KEYBOARD)[0]
        self.keys = keyboard.leds
        index = 0
        for key in self.keys:
            name = key.name
            if name != 'Unused':
                name = key.name[5:].replace(' ', '_')
                self.data[name] = {'x': None,
                                   'y': None,
                                   'id': index}
            else:
                self.unused_leds.append(index)
            index += 1
        self.num_leds = index - 1

    def K_Escape(self, x=0, y=0):
        name = 'Escape'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Circumflex(self, x=0, y=0):
        name = '^'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Tab(self, x=0, y=0):
        name = 'Tab'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Caps_Lock(self, x=0, y=0):
        name = 'Caps_Lock'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Left_Shift(self, x=0, y=0):
        name = 'Left_Shift'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Left_Control(self, x=0, y=0):
        name = 'Left_Control'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_1(self, x=0, y=0):
        name = '1'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Q(self, x=0, y=0):
        name = 'Q'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_A(self, x=0, y=0):
        name = 'A'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Lessthan(self, x=0, y=0):
        name = '<'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Left_Windows(self, x=0, y=0):
        name = 'Left_Windows'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_F1(self, x=0, y=0):
        name = 'F1'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_2(self, x=0, y=0):
        name = '2'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_W(self, x=0, y=0):
        name = 'W'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_S(self, x=0, y=0):
        name = 'S'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Y(self, x=0, y=0):
        name = 'Y'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Left_Alt(self, x=0, y=0):
        name = 'Left_Alt'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_F2(self, x=0, y=0):
        name = 'F2'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_3(self, x=0, y=0):
        name = '3'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_E(self, x=0, y=0):
        name = 'E'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_D(self, x=0, y=0):
        name = 'D'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_X(self, x=0, y=0):
        name = 'X'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_F3(self, x=0, y=0):
        name = 'F3'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_4(self, x=0, y=0):
        name = '4'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_R(self, x=0, y=0):
        name = 'R'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_F(self, x=0, y=0):
        name = 'F'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_C(self, x=0, y=0):
        name = 'C'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_F4(self, x=0, y=0):
        name = 'F4'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_5(self, x=0, y=0):
        name = '5'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_T(self, x=0, y=0):
        name = 'T'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_G(self, x=0, y=0):
        name = 'G'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_V(self, x=0, y=0):
        name = 'V'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_6(self, x=0, y=0):
        name = '6'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Z(self, x=0, y=0):
        name = 'Z'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_H(self, x=0, y=0):
        name = 'H'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_B(self, x=0, y=0):
        name = 'B'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Space(self, x=0, y=0):
        name = 'Space'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_F5(self, x=0, y=0):
        name = 'F5'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_7(self, x=0, y=0):
        name = '7'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_U(self, x=0, y=0):
        name = 'U'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_J(self, x=0, y=0):
        name = 'J'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_N(self, x=0, y=0):
        name = 'N'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_F6(self, x=0, y=0):
        name = 'F6'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_8(self, x=0, y=0):
        name = '8'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_I(self, x=0, y=0):
        name = 'I'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_K(self, x=0, y=0):
        name = 'K'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_M(self, x=0, y=0):
        name = 'M'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_F7(self, x=0, y=0):
        name = 'F7'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_9(self, x=0, y=0):
        name = '9'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_O(self, x=0, y=0):
        name = 'O'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_L(self, x=0, y=0):
        name = 'L'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Comma(self, x=0, y=0):
        name = ','
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_F8(self, x=0, y=0):
        name = 'F8'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_0(self, x=0, y=0):
        name = '0'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_P(self, x=0, y=0):
        name = 'P'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_OE(self, x=0, y=0):
        name = 'Ö'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Dot(self, x=0, y=0):
        name = '.'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Right_Alt(self, x=0, y=0):
        name = 'Right_Alt'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Sharp_S(self, x=0, y=0):
        name = 'ß'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_UE(self, x=0, y=0):
        name = 'Ü'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_AE(self, x=0, y=0):
        name = 'Ä'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Minus(self, x=0, y=0):
        name = '-'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Right_Fn(self, x=0, y=0):
        name = 'Right_Fn'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_F9(self, x=0, y=0):
        name = 'F9'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Acute_Accent(self, x=0, y=0):
        name = '´'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Plus(self, x=0, y=0):
        name = '+'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Right_Shift(self, x=0, y=0):
        name = 'Right_Shift'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Menu(self, x=0, y=0):
        name = 'Menu'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_F10(self, x=0, y=0):
        name = 'F10'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_F11(self, x=0, y=0):
        name = 'F11'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_F12(self, x=0, y=0):
        name = 'F12'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Backspace(self, x=0, y=0):
        name = 'Backspace'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Enter(self, x=0, y=0):
        name = 'Enter'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Right_Control(self, x=0, y=0):
        name = 'Right_Control'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Hashtag(self, x=0, y=0):
        name = '#'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Print_Screen(self, x=0, y=0):
        name = 'Print_Screen'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Insert(self, x=0, y=0):
        name = 'Insert'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Delete(self, x=0, y=0):
        name = 'Delete'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Left_Arrow(self, x=0, y=0):
        name = 'Left_Arrow'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Scroll_Lock(self, x=0, y=0):
        name = 'Scroll_Lock'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Home(self, x=0, y=0):
        name = 'Home'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_End(self, x=0, y=0):
        name = 'End'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Up_Arrow(self, x=0, y=0):
        name = 'Up_Arrow'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Down_Arrow(self, x=0, y=0):
        name = 'Down_Arrow'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Pause_Break(self, x=0, y=0):
        name = 'Pause/Break'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Page_Up(self, x=0, y=0):
        name = 'Page_Up'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Page_Down(self, x=0, y=0):
        name = 'Page_Down'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Right_Arrow(self, x=0, y=0):
        name = 'Right_Arrow'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Num_Lock(self, x=0, y=0):
        name = 'Num_Lock'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_7(self, x=0, y=0):
        name = 'Number_Pad_7'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_4(self, x=0, y=0):
        name = 'Number_Pad_4'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_1(self, x=0, y=0):
        name = 'Number_Pad_1'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_0(self, x=0, y=0):
        name = 'Number_Pad_0'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_Slash(self, x=0, y=0):
        name = 'Number_Pad_/'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_8(self, x=0, y=0):
        name = 'Number_Pad_8'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_5(self, x=0, y=0):
        name = 'Number_Pad_5'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_2(self, x=0, y=0):
        name = 'Number_Pad_2'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_Star(self, x=0, y=0):
        name = 'Number_Pad_*'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_9(self, x=0, y=0):
        name = 'Number_Pad_9'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_6(self, x=0, y=0):
        name = 'Number_Pad_6'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_3(self, x=0, y=0):
        name = 'Number_Pad_3'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_Comma(self, x=0, y=0):
        name = 'Number_Pad_,'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_Minus(self, x=0, y=0):
        name = 'Number_Pad_-'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_Plus(self, x=0, y=0):
        name = 'Number_Pad_+'
        self.data[name]['x'] = x
        self.data[name]['y'] = y

    def K_Number_Pad_Enter(self, x=0, y=0):
        name = 'Number_Pad_Enter'
        self.data[name]['x'] = x
        self.data[name]['y'] = y