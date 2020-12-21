import paho.mqtt.client as mqtt
import base64
import mysql.connector
MQTT_SERVER = "192.168.57.102"
MQTT_PATH = "Image"
import datetime
import config

//Tietokantayhteyden määrittely, tiedot toisessa tiedostossa config.py
db_connection=mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.passwd,
    database=config.database
)

//Funktio kuvan tietojen lisäämiseen tietokantaan
def to_database(name):
    db_cursor= db_connection.cursor()
    url="http://192.168.9.40/~administrator/pikuvat/"+name+".jpg"
    image_sql_query="Insert INTO images(name,url,time) VALUES (%s,%s,%s)"
    db_cursor.execute(image_sql_query, (name, url, name))
    db_connection.commit()
    print("Image inserted")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(MQTT_PATH)


def on_message(client, userdata, msg):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    msg_payload = msg.payload.decode()
    msg_decoded=base64.b64decode(msg_payload)
    with open('public_html/pikuvat/'+timestamp+'.jpg', 'wb') as f:
        f.write(msg_decoded)
        to_database(timestamp)
    
    print("Image Received")
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)


client.loop_forever()
