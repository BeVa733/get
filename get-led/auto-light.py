import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


light = 6
led = 26
state = 0

GPIO.setup(led, GPIO.OUT)
GPIO.setup(light, GPIO.IN)

while True:
    state = GPIO.input(light)
    GPIO.output(led, not state)
    time.sleep(0.2)