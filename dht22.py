#!/usr/bin/python3
from mqtt_publish import sendpayload
import Adafruit_DHT
import time
import json

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def calibrate(val, offSet):
  return val + offSet

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        temp_to_fahrenheit = temperature *1.8 + 32
        time.sleep(5)
        tempOffSet = -1.5
        humidityOffSet = -5
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(calibrate(temp_to_fahrenheit, tempOffSet), calibrate(humidity, humidityOffSet)))
        payload = {
          "temperature": calibrate(temp_to_fahrenheit, tempOffSet),
          "humidity": calibrate(humidity, humidityOffSet),
        }
        json_payload = json.dumps(payload)
      
        sendpayload("JTL/temps/plant1", json_payload)
    else:
        print("Failed to retrieve data from humidity sensor")

