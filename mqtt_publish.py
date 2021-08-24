import paho.mqtt.client as mqtt
from dotenv import load_dotenv
load_dotenv()
import os

def sendpayload(topic, payload):
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code", rc)
        # topic, payload=None, qos=0, retain=False
        client.publish(topic, payload)
        print("Message sent. Disconnecting...")
        client.disconnect()

    client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
    client.on_connect = on_connect

    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')

    client.username_pw_set(username, password)
    print("Connecting...")

    host = os.environ.get('HOST')
    port = int(os.environ.get('PORT'))
    keepalive = 60
    client.connect(host, port, keepalive)
    client.loop_forever()

# need to setup env vars for user and password