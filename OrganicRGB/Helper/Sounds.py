import threading
from math import isnan

import numpy as np
import soundcard as sc
from numba import njit
from scipy.fft import rfft, rfftfreq

class Recorder():
    # power
    save_last = 2  # seconds
    shorttime_average_power = 0.5
    y_power = 0.75
    target_average = 0.4
    rel_multiplier_relewance = 1.25
    power_cut = 0.0

    def __init__(self, sample_rate: int, record_length: float, freq_division: list[int]) -> None:  # record_length in ms
        self.loop = True
        self.sound_thread = threading.Thread(target=self.mainloop)
        
        self.sample_rate = sample_rate
        self.record_length = record_length / 1000  # r
        self.buffer_size = self.sample_rate * self.record_length
        self.freq_division = np.array(freq_division, dtype=np.uint16)

        self.loopback = sc.get_microphone(include_loopback=True, id=sc.default_speaker().id)
        self.buffer = np.zeros((int(self.buffer_size), 2), dtype=np.float64)
        
        self.fft_y = None
        self.fft_x = None
        self.data = None
        self.beat_power = None
        self.frequency_strengths = None
        
        self.power_level_history = np.zeros(int(self.save_last / self.record_length), dtype=np.float64)
        
    def start(self) -> None:
        self.sound_thread.start()
        
    def stop(self) -> None:
        self.loop = False
        self.sound_thread.join()
        
    @staticmethod
    @njit(fastmath=True)
    def get_freq_strengths(fft_x: np.ndarray['N', np.dtype[np.float64]], fft_y: np.ndarray['N', np.dtype[np.float64]],
                           freq_division: np.ndarray['N', np.dtype[np.float64]]) -> np.ndarray[
        'N', np.dtype[np.float64]]:
        num_freq_division = len(freq_division) - 1
        freq_strengths = np.zeros(num_freq_division, dtype=np.float64)
        active_freq = 0
        
        for x, y in zip(fft_x, fft_y):
            if active_freq < num_freq_division:
                if x > freq_division[active_freq + 1]:
                    active_freq += 1
                elif freq_division[active_freq] < x < freq_division[active_freq + 1]:
                    freq_strengths[active_freq] += y
        for a in range(0, num_freq_division):
            freq_strengths[a] = freq_strengths[a] / (freq_division[a + 1] - freq_division[a])
            
        return freq_strengths * 2

    @staticmethod
    @njit(fastmath=True)
    def db_to_dbA(fft_x: np.ndarray['N', np.dtype[np.float64]], fft_y: np.ndarray['N', np.dtype[np.complex64]]) -> \
    np.ndarray['N', np.dtype[np.float64]]:
        fft_y = np.abs(fft_y)
        index = 0
        new_fft_y = np.zeros(len(fft_y), dtype=np.float64)
        for x, y in zip(fft_x, fft_y):
            kB = 5.99185 * 10 ** 9
            ugA = (x + 129.4) ** 2 * (x + 995.9) * (x + 76655) ** 2
            gA = (kB * x ** 3) / ugA
            new_fft_y[index] = y * gA
            index += 1
        return new_fft_y

    def get_power(self, data: np.ndarray['N', np.dtype[np.float64]], chunk_size: int, sample_rate: int) -> tuple[
        float, np.ndarray['N', np.dtype[np.float64]], np.ndarray['N', np.dtype[np.float64]]]:
        fft_y = rfft(data, n=int(chunk_size * 8), workers=-1)
        fft_x = rfftfreq(int(chunk_size * 8), 1 / (sample_rate))
        fft_y = self.db_to_dbA(fft_x, fft_y)
        power_level = (np.sum(fft_y)*2) / chunk_size
        return power_level, fft_y, fft_x

    def mainloop(self) -> None:
        with self.loopback.recorder(self.sample_rate, 2, 16) as recorder:
            while self.loop:
                self.buffer = recorder.record(len(self.buffer))  # get audio data

                # calc raw data
                single_channel_buffer = np.sum(self.buffer, axis=1) / 2

                fft_y = rfft(single_channel_buffer, n=int(self.buffer_size), workers=-1)
                self.fft_x = rfftfreq(int(self.buffer_size), 1 / self.sample_rate)

                self.fft_y = self.db_to_dbA(self.fft_x, fft_y)

                #self.beat_power, self.fft_y, self.fft_x = self.get_power(single_channel_buffer, int(self.buffer_size), self.sample_rate)

                # calc beat power
                self.beat_power = np.sum(np.abs(self.buffer)) / len(self.buffer)
                self.power_level_history = np.concatenate(
                    (np.array([self.beat_power], dtype=np.float64), self.power_level_history[0:-1]), axis=0)
                power_avg = np.sum(self.power_level_history) / int(self.save_last / self.record_length)
                if power_avg != 0:
                    rel_multiplier = self.target_average / power_avg ** self.rel_multiplier_relewance
                    rel_power_level = self.beat_power * rel_multiplier
                    self.shorttime_average_power = rel_power_level * self.y_power + self.shorttime_average_power * (
                                1 - self.y_power)
                else:
                    self.shorttime_average_power = 0

                if self.shorttime_average_power > 1:
                    self.shorttime_average_power = 1
                elif self.shorttime_average_power < self.power_cut or isnan(self.shorttime_average_power):
                    self.shorttime_average_power = 0

                self.shorttime_average_power -= self.power_cut
                self.shorttime_average_power /= 1 - self.power_cut

                # calc frequency strenghts
                if self.beat_power != 0:
                    self.frequency_strengths = self.get_freq_strengths(self.fft_x, self.fft_y, self.freq_division) / (
                                self.beat_power ** 0.75 * 3)
                else:
                    self.frequency_strengths *= 0
                self.frequency_strengths = np.clip(self.frequency_strengths, 0, 1)

    def get_rawdata(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        return self.buffer, self.fft_x, self.fft_y

    def get_data(self) -> tuple[float, np.ndarray]:
        return self.shorttime_average_power, self.frequency_strengths