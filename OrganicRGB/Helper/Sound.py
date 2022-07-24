import soundcard as sc
import numpy as np
import pygame
from math import log, isnan, log10
from scipy.fft import rfft, rfftfreq
from matplotlib import pyplot as plt

class helper:
    sample_rate = 48000
    use_fft = False
    beat_power_method = 1
    fft_length = 6 # 20 - 20000hz

    chunk_size = 1024
    relative_sec = 2
    initial_power_multiplier = 50
    y = 0.75
    cut_point = 0.08
    target_average = 0.55
    rel_multiplier_relewance = 0.75
    fft_start_end = [1.30103, 4.30103]
    fft_range = []

    last_data = [0, []]
    history_num = [int((sample_rate * relative_sec) / chunk_size), 0]
    power_level_history = np.zeros(history_num[0], dtype='double')
    shorttime_average_power = 0.5

    running = True

    def __init__(self, fft=False, sample_rate=48000, beat_power_method=1, multiplier=50, fft_length=6):
        default_speaker = sc.default_speaker()
        self.loopback = sc.get_microphone(include_loopback=True, id=default_speaker.id)
        self.use_fft = fft
        self.sample_rate = sample_rate
        self.beat_power_method = beat_power_method
        self.initial_power_multiplier = multiplier
        self.fft_length = fft_length
        if self.use_fft:
            start = log10(20)
            end = log10(20000)
            for a in range(0, fft_length+1):
                exponent = start + ((end-start)/fft_length)*a
                self.fft_range.append(10**exponent)
        self.fft_range = [20, 250, 600, 4000, 6000, 8000, 20000]
        print(self.fft_range)

    def mainloop(self):
        data = self.loopback.record(samplerate=self.sample_rate, numframes=self.chunk_size, channels=2, blocksize=64)

        #compute fft
        if self.use_fft:
            fft_finished = np.zeros(self.fft_length, dtype='double')
            fft_active = 0
            fft_data = []
            for dat in data:
                fft_data.append((dat[0] + dat[1]) / 2)
            fft_data = np.array(fft_data)
            fft_y = rfft(fft_data, n=int(self.chunk_size* 2), workers=-1)
            fft_x = rfftfreq(int(self.chunk_size * 2), 1 / (self.sample_rate))
            for x, y in zip(fft_x, np.abs(fft_y)):

                if fft_active < self.fft_length:
                    if x > self.fft_range[fft_active+1]:
                        fft_active += 1
                    elif self.fft_range[fft_active] < x < self.fft_range[fft_active+1]:
                        #print(y)
                        fft_finished[fft_active] += y
            for a in range(0, self.fft_length):
                fft_finished[a] = fft_finished[a] / (self.fft_range[a+1] - self.fft_range[a])
            self.last_data[1] = fft_finished


        #compute power level
        power_level = (np.sum(np.abs(data)) * self.initial_power_multiplier) / (2 * self.sample_rate)
        if self.beat_power_method == 0:
            self.last_data[0] = self.shorttime_average_power * power_level

        elif self.beat_power_method == 1:
            self.power_level_history = np.concatenate((np.array([power_level], dtype='double'), self.power_level_history[0:-1]),
                                                 axis=0)
            if self.history_num[1] < self.history_num[0]:
                self.history_num[1] += 1
            power_avg = np.sum(self.power_level_history) / self.history_num[1]
            #power_min = np.min(self.power_level_history)
            #power_max = np.max(self.power_level_history)

            if power_avg != 0:
                rel_multiplier = self.target_average / power_avg ** self.rel_multiplier_relewance
                rel_power_level = power_level * rel_multiplier
                self.shorttime_average_power = rel_power_level
                self.shorttime_average_power = rel_power_level * self.y + self.shorttime_average_power * (1 - self.y)
            else:
                self.shorttime_average_power = 0

            #self.shorttime_average_power = (self.shorttime_average_power - self.cut_point) / (1 - self.cut_point)
            if self.shorttime_average_power > 1: self.shorttime_average_power = 1
            elif self.shorttime_average_power < 0 or isnan(self.shorttime_average_power): self.shorttime_average_power = 0

            self.last_data[0] = self.shorttime_average_power

    def get_last_data(self):
        return tuple(self.last_data)