Welcome to the furnace wiki!
This describes how to setup the raspberry pi with basic step by step instructions for monitoring temperatures.

The python scrips provided will read the sensor data and output it with numeric values in Fahrenheit only, for upload to thingspeak.com as the platform.

First steps are to install Raspbian Lite onto the sd card. I'm not going to be going over those details.

once that's done, we'll place 2 files on the pi so that it will connect to our network and enable ssh by default

SSH configuration
on the /boot directly, create a file named ssh it does not need any file extension or any contents. it's existence at boot will tell the pi to enable ssh

wifi configuration
Create a file called wpa_supplicant.conf and place it on the root of the pi as well. these values will be read into the raspberry pi wifi configuration at boot. the file is deleted afterwards. You can supply multiple values if you want it to try more then one wifi connection. I have a sample in the files section.

Operation System config to enable temperature and gpio related pins.
Edit /etc/modules/ and add these 2 to the bottom if they don't exist. save the file. w1_gpio w1_therm

modify /boot/config.txt to enable the use of the GPIO pins (to activate them)

dtoverlay=w1-gpio,gpiopin=4 dtoverlay=w1-gpio,gpiopin=26

the first line is for the standard usage of gpiopin 4 which is basically whatever every wiring guide uses for the 1 wire bus system. the additional line is to enable me to use gpiopin 26 as I will be attaching both ds18b20 sensors (can share the gpiopin4) and 1 dht22 (must have dedicated 1 wire bus on 26)

DHT22 specific configuration
below is required for the DHT22 sensor to function

git clone https://github.com/adafruit/Adafruit_Python_DHT.git

cd Adafruit_Python_DHT

sudo apt-get update

sudo apt-get install build-essential python-dev

sudo python setup.py install
