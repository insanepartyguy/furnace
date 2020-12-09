#!/usr/bin/env python

#Libraries
import Adafruit_DHT as dht
import time
import requests
#Set DATA pin
DHT = 26
#while True:
#Read Temp and Hum from DHT22
h,t = dht.read_retry(dht.DHT22, DHT)
#Print Temperature
print('{0:0.1f}'.format(t,h))
#Print Humidity
print('{1:0.1f}'.format(t,h))
#send data to thingspeak via GET request
url = 'http://api.thingspeak.com/update.json'
myobj = {'api_key': 'REDACTED','field6': '{0:0.1f}'.format(t,h),'field5': '{1:0.1f}'.format(t,h)}
x = requests.get(url, data = myobj)
