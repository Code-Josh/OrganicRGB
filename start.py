from OrganicRGB import main as orgb
import json

RedBlue = './ColorProfiles/RedBlue.json'
YellowBlue = './ColorProfiles/YellowBlue.json'
Pastell = './ColorProfiles/Pastell.json'

def start(profile_path):
    with open(profile_path, 'r') as file:
        settings = json.loads(file.read())
        color_settings = settings['color_settings']
        noise_settings = settings['noise_settings']
        music_settings = settings['music_settings']
        devices = settings['devices']
        MainSetup = orgb.main(color_settings, noise_settings, music_settings)
        print(MainSetup.get_Devices())
        MainSetup.activate_Device('Keyboard')
        MainSetup.show2D(234, 463)

if __name__ == '__main__':
    start(RedBlue)