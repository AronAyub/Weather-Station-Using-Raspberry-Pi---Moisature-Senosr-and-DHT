# Weather Station Using Raspberry Pi , Moisature Senosr and DHT
 Make a home weather mini weather station 

 - The most critical part of this project is on how to use circuitpython Library on Rapberry Pi.

 ## Prerequisite Pi Setup!
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

**Update RPi and Python**

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
``