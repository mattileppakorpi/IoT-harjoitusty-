from picamera import PiCamera
from time import sleep

import RPi.GPIO as GPIO
import time

sound = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(sound, GPIO.IN)

camera = PiCamera()


while True:
    if GPIO.wait_for_edge(sound, GPIO.RISING):
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Desktop/image.jpg')
        camera.stop_preview()

