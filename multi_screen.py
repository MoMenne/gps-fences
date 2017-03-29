#!/usr/bin/env python
import time
import socket
import signal
import pdb
from gps_thread import GpsPoller
from internet_thread import InternetPoller

import dothat.backlight as backlight
import dothat.lcd as lcd
import dothat.touch as nav


# this makes it easy to find the local IP
from netifaces import interfaces, ifaddresses, AF_INET

print("""
        Running GPS via the Raspberry Pi
""")
screens = ["gps", "internet"]
current_screen = 0 

@nav.on(nav.LEFT)
def handle_switch(ch, evt):
	print("switching left!")
	lcd.clear()
	lcd.write("Left")
        current_screen -= 1

@nav.on(nav.RIGHT)
def handle_switch_right(ch, evt):
	print("switching right!")
	lcd.clear()
	lcd.write("Right")
        current_screen += 1

if __name__ == '__main__':
    gpsp = GpsPoller()
    internet_poller = InternetPoller()
    try:
        gpsp.start()
        while True:
            if current_screen % 2 == 0:
                print "GPS"
                lcd.set_cursor_position(0,0)
                lcd.write("heading " + "%.2f" % gpsd.fix.track )
                lcd.set_cursor_position(0,1)
                lcd.write("lat  " + "%.5f" % gpsd.fix.latitude )
                lcd.set_cursor_position(0,2)
                lcd.write("long " + "%.5f" % gpsd.fix.longitude)
            else:
                print "Internet"
            time.sleep(5)
            
    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        print "Shutting it down\n"
        gpsp.running = False
        gpsp.join()

    print "All Done.  Exiting"
