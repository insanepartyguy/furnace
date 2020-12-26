#!/usr/bin/env python

#Libraries
import Adafruit_DHT as dht
import time
import requests
#Set DATA pin
DHT = 26
#Read Temp and Hum from DHT22
h,t = dht.read_retry(dht.DHT22,DHT)
h_round = round(h, 1)
t_f = round((t * 9.0 / 5.0 + 32.0),1)
#print(h_round,t_f)
#send data to thingspeak via GET request
url = 'http://api.thingspeak.com/update.json'
myobj = {'api_key': 'REDACTED','field6': '{0:0.1f}'.format(t_f,h_round),'field5': '{1:0.1f}'.format(t_f,h_round)}
x = requests.get(url, data = myobj)
