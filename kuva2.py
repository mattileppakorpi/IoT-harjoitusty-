from picamera import PiCamera
from time import sleep

#import RPi.GPIO as GPIO
import time
import base64
import paho.mqtt.client as mqtt

client = mqtt.client()
timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(sound, GPIO.IN)

camera = PiCamera()

camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg', resize=(500, 281))
    camera.close()
convertImageToBase64()

def convertImageToBase64():
 with open("/home/pi/Desktop/image.jpg", "rb") as image_file:
 encoded = base64.b64encode(image_file.read())
 return encoded