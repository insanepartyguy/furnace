#!/usr/bin/env python

#Libraries
import Adafruit_DHT as dht
import time
#Set DATA pin
DHT = 26
#while True:
#Read Temp and Hum from DHT22
h,t = dht.read_retry(dht.DHT22, DHT)
#Print Temperature and Humidity on Shell window
#print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t,h))
print('{0:0.1f}'.format(t,h))
print('{1:0.1f}'.format(t,h))
