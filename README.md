# Weather Station Using Raspberry Pi, Azure , Moisture, Temp & Hum.

 Make a home weather mini weather station 

 - The most critical part of this project is on how to use circuitpython Library on Rapberry Pi.

 ## Prerequisite R-Pi Setup!
In this page we'll assume you've already gotten your Raspberry Pi up and running and can log into the command line

- Here's the quick-start for people with some experience:However, be encouraged to use any method of your choice to install the OS.

1. Download the latest Raspberry Pi OS or [Raspberry Pi OS Lite to your computer](https://www.raspberrypi.com/software/operating-systems/)
2. Burn the OS image to your [MicroSD card using your computer](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi)
3. [Re-plug the SD card into your computer (don't use your Pi yet!) and set up your wifi connection by editing supplicant.conf](https://learn.adafruit.com/raspberry-pi-zero-creation/text-file-editing)
3. Activate SSH support
4. Plug the SD card into the Pi
5. If you have an HDMI monitor we recommend connecting it so you can see that the Pi is booting OK
6. Plug in power to the Pi - you will see the green LED flicker a little. The Pi will reboot while it sets up so wait a good 10 minutes
7. You can then ssh into raspberrypi.local

- Follow instructions below:

**Update RPi and Python**

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
```

**Update Setup Tools**

```
sudo pip3 install --upgrade setuptools
```
-  We put together a script to easily make sure your Pi is correctly configured and install Blinka. It requires just a few commands to run. Most of it is installing the dependencies.

```
cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
```

**Installing the CircuitPython-DHT Library**

- You'll also need to install a library to communicate with the DHT sensor. Since we're using Adafruit Blinka (CircuitPython), we can install CircuitPython libraries straight to our small linux board. In this case, we're going to install the CircuitPython_DHT library. This library works with both the DHT22 and DHT11 sensors.

* Run the following command to install the CircuitPython-DHT library:

```
pip3 install adafruit-circuitpython-dht

sudo apt-get install libgpiod2
```
**Testing the Library**
Testing the CircuitPython DHT Library
To make sure you've installed everything correctly, we're going to test that we can read values from the DHT sensor connected to your device.

- Create a new file called dht_simpletest.py with nano or your favorite text editor and put the following in:
- Run the example below:


```
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D18)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)

```

* **NB** *Next, you're going to need to modify a line of code in this file with information about the pin the DHT sensor is connected to and the type of DHT sensor you're using.*

- If you're using a Raspberry Pi with a DHT22 (or an AM2302) sensor connected to Pin 4, change the following line from:

```
dhtDevice = adafruit_dht.DHT22(board.D18)
```
to

```
dhtDevice = adafruit_dht.DHT22(board.D4)
```
- If you're using a BeagleBone Black with a DHT22 (or an AM2302) sensor connected to Pin P8_11, change the following line from

```
dhtDevice = adafruit_dht.DHT22(board.D18)
```

to 

```
dhtDevice = adafruit_dht.DHT22(board.P8_11)
```

- If you're using a DHT11 sensor, you can change the sensor type by renaming the DHT22 class to DHT11:

```
dhtDevice = adafruit_dht.DHT11(board.D18)
```

* Then, save the example. Next, run the example by typing the following command into the terminal:

python3 dht_simpletest.py

* Press enter to run the example. You should see the temperature (in Fahrenheit and Celsius) and humidity values displayed in the terminal:
