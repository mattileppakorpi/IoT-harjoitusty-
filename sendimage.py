from time import sleep
from picamera import PiCamera
import time
import base64
import paho.mqtt.publish as publish # vai client?

timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

camera = PiCamera()
camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Desktop/image.jpg', resize=(500, 281))
    camera.close()
    convertImageToBase64() #tarviiko tätä tehdä?

def convertImageToBase64():
 with open("/home/pi/Desktop/image.jpg", "rb") as image_file:
     encoded = base64.b64encode(image_file.read())
 return encoded


MQTT_SERVER = "192.168.9.40"  #Write Server IP Address
MQTT_PATH = "Image"

f=open("i/home/pi/Desktop/image.jpg", "rb") 
fileContent = f.read()
byteArr = bytearray(fileContent)


publish.single(MQTT_PATH, byteArr, hostname=MQTT_SERVER)