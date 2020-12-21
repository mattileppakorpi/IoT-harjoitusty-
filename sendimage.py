from picamera import PiCamera
import time
import datetime
import base64
import paho.mqtt.publish as publish

timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')//Tämä jäi turhaksi

//funktio kuvan muuntamiseen
def convertImageToBase64():
 with open("/home/pi/Desktop/image.jpg", "rb") as image_file:
     encoded = base64.b64encode(image_file.read())
 return encoded

//Otetaan kuva
camera = PiCamera()
camera.start_preview()
sleep(3)//kameralle aikaa käynnistyä
camera.capture('/home/pi/Desktop/image.jpg', resize=(500, 281))
camera.close()
image64= convertImageToBase64()

//Lähetetään kuva
MQTT_SERVER = "192.168.57.102"
MQTT_PATH = "Image"

publish.single(MQTT_PATH, image64, hostname=MQTT_SERVER, port=1883)
