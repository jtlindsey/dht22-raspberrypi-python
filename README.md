# README

- DFRobot DHT22 pinout
  - left green pin is data/signal, middle red is vcc/5v, and right black is GND
- RaspberryPi 


| Left     	|   	|   	| Right  	|
|----------	|---	|---	|--------	|
| 3.3v PWR 	| 1 	| 2 	| 5V PWR 	|
| GPIO 2   	| 3 	| 4 	| 5V PWR 	|
| GPIO 3   	| 5 	| 6 	| GND    	|
| GPIO 4   	| 7 	| 8 	| UARTO TX|


## Dependencies
python3 and setup tools
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-dev python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT
```

MQTT library
https://www.eclipse.org/paho/index.php?page=clients/python/index.php
`pip install paho-mqtt`
Install with root home target for use in systemd script `(-H)`
`sudo -H pip install paho-mqtt`


Reading ENV vars
`pip install python-dotenv`
Install with root home target for use in systemd script `(-H)`
`sudo -H pip install python-dotenv`

## Example `.env`
```
USERNAME=appuser1
PASSWORD=password1
HOST=192.168.10.226
PORT=1883
```

## Basic Usage
`python3 dht22.py`


## Systemd Usage

### Create script

Run the following command and add the script data:
`sudo vi /etc/systemd/system/dht22.service`

```
[Unit]
Description=Send temperature and humidity values via MQTT
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/Documents/tempAndHumidity/dht22.py

[Install]
WantedBy=multi-user.target
```

### Systemd Commands

```
chmod ugo+x dht22.py
systemctl enable dht22.service
systemctl start dht22.service
systemctl status dht22.service
systemctl stop dht22.service

# The text output of the script you will find in the journal:
journalctl -b -e
```

## dht22 code ref
https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/
Installation

## Notes

if context worked you could do the following but it doesnt work with python3
```
import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish

username="appuser1"
password="password1"
host = "192.168.10.226"
port = 1883
qos = 0
retain = False
client_id = ""
keepalive = 60
will=None
auth = { 'username': username, 'password': password }
tls=None
protocol=mqtt.MQTTv311,
transport="tcp"
topic = "JTL/temps/plant1"
payload = "This is a test..."


publish.single(topic,
    payload,
    qos,
    retain,
    host,
    port,
    client_id,
    keepalive,
    will,
    auth,
    tls,
    protocol,
    transport
)

```