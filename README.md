gps-fences
==========

This project uses a GlobalSat BU-353 receiver to pull the GPS coordinates of a raspberry pi.

Instructions
* To get started, use etcher.io to flash an SD card with an image of the latest Raspberry pi image
* Follow this [blog post](https://www.raspberrypi.org/forums/viewtopic.php?&t=32461) to get the Raspberry Pi set up for GPS.
* Here's an [article about setting up wifi on a raspberry pi](http://raspberrypihq.com/how-to-add-wifi-to-the-raspberry-pi/) 
* To look at the gps output run `gpsmon /dev/ttyUSB0`
* This [blog post](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=138711) was essential to getting the BU-353 working with the Pi.
