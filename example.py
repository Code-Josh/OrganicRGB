from OrganicRGB import main as orgb

color_settings_1 = {
        'colorpalette': [(0, 120, 0), (0, 0, 220), (255, 255, 128)],
        'saturation': 2,
        'value': 0.6
    }

noise_settings_1 = {
    'speed': 100,
    'feature_size': 100,
    'seed': 3684
}

color_settings_2 = {
        'colorpalette': [(180, 0, 0), (255, 200, 0)],#, (255, 0, 0)],
        'saturation': 2,
        'value': 0.6
    }

noise_settings_2 = {
    'speed': 50,
    'feature_size': 100,
    'seed': 3684
}
music_settings = {
    'beat': False,
    'color': (0, 0, 0)
}

MainSetup = orgb.main(color_settings_2, noise_settings_2, music=music_settings)
MainSetup.set_case(520, 496, 230)
print(MainSetup.get_Devices())
MainSetup.activate_Device('Keyboard')
MainSetup.show2D(234, 463)
