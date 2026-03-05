import RPi.GPIO as GPIO 
import signal_generator as sgen 
import time
import pwm_dac

amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pwm_dac.PWM_DAC(12, 500, 3.290, True)
    start_time = time.time()
    while True:
        current_time = time.time() - start_time
        signal = amplitude * sgen.get_sin_wave_amplitude(signal_frequency, current_time)
        dac.set_voltage(signal)
        sgen.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()