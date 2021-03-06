#!/usr/bin/env python3

import os
import glob
import time

BASE_DIR = '/sys/bus/w1/devices'
DEVICES = {
    'Outside Temperature': '28-021480dea3ff',
    'Incoming': '28-0317304f88ff',
    'To Storage': '28-0317604c0fff',
    'House Feed': '28-0417302868ff'
}
DEVICE_FILE = '/w1_slave'

def read_temp(device):
    with open(device, 'r') as f:
        lines = f.readlines()

        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return round(temp_f, 2)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

#while True:
for label, device_id in DEVICES.items():
    print(current_time +"  " + label + " : " + str(read_temp(f"{BASE_DIR}/{device_id}/{DEVICE_FILE}")))
