#!/usr/bin/env python
import time
import socket
import signal
import pdb
import logging
from gps_thread import GpsPoller
from internet_thread import InternetPoller
from zone_thread import ZonePoller

import dothat.backlight as backlight
import dothat.lcd as lcd
import dothat.touch as nav


# this makes it easy to find the local IP
from netifaces import interfaces, ifaddresses, AF_INET

logging.basicConfig(filename="logs/application.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s-%(message)s')

logging.debug("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Starting up Raspi GPS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

current_screen = 0 
screens = ["gps", "internet", "zone"]

@nav.on(nav.LEFT)
def handle_switch(ch, evt):
	logging.debug("switching left!")
	lcd.clear()
        global current_screen
        current_screen -= 1

@nav.on(nav.RIGHT)
def handle_switch_right(ch, evt):
	logging.debug("switching right!")
	lcd.clear()
        global current_screen
        current_screen += 1

if __name__ == '__main__':
    gpsp = GpsPoller()
    internet_poller = InternetPoller()
    zone_poller = ZonePoller(gpsp)
    try:
        gpsp.start()
        internet_poller.start()
        zone_poller.start()
        time.sleep(1)
        logging.debug("starting ip address %s", internet_poller.eth0_address[0])
        logging.debug("starting gps data %.2f %.5f %.5f", gpsp.gpsd.fix.track, gpsp.gpsd.fix.latitude, gpsp.gpsd.fix.longitude)
        while True:
            if current_screen % 3 == 0:
                lcd.clear
                lcd.set_cursor_position(0,0)
                lcd.write("heading " + "%.2f" % gpsp.gpsd.fix.track )
                lcd.set_cursor_position(0,1)
                lcd.write("lat  " + "%.5f" % gpsp.gpsd.fix.latitude )
                lcd.set_cursor_position(0,2)
                lcd.write("long " + "%.5f" % gpsp.gpsd.fix.longitude)
            elif current_screen % 3 == 1:
                lcd.clear
                lcd.set_cursor_position(5,0)
                lcd.write("Zone")
                lcd.set_cursor_position(0,2)
                lcd.write(zone_poller.current_zone)
            else:
                lcd.clear()
                lcd.set_cursor_position(0,2)
                lcd.write(internet_poller.eth0_address[0])
                lcd.set_cursor_position(13,2)
                lcd.write(internet_poller.status)
            time.sleep(1)
            
    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        logging.debug("Shutting it down")
        gpsp.running = False
        gpsp.join()

    logging.debug("All Done.  Exiting")
