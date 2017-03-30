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

current_screen = 0 
screens = ["gps", "internet"]

@nav.on(nav.LEFT)
def handle_switch(ch, evt):
	print("switching left!")
	lcd.clear()
        global current_screen
        current_screen -= 1

@nav.on(nav.RIGHT)
def handle_switch_right(ch, evt):
	print("switching right!")
	lcd.clear()
        global current_screen
        current_screen += 1

if __name__ == '__main__':
    print "running main"
    gpsp = GpsPoller()
    internet_poller = InternetPoller()
    try:
        gpsp.start()
        internet_poller.start()
        while True:
            if current_screen % 2 == 0:
                lcd.clear
                lcd.set_cursor_position(0,0)
                lcd.write("heading " + "%.2f" % gpsp.gpsd.fix.track )
                lcd.set_cursor_position(0,1)
                lcd.write("lat  " + "%.5f" % gpsp.gpsd.fix.latitude )
                lcd.set_cursor_position(0,2)
                lcd.write("long " + "%.5f" % gpsp.gpsd.fix.longitude)
            else:
                lcd.clear()
                lcd.set_cursor_position(0,2)
                lcd.write(internet_poller.eth0_address[0])
                lcd.set_cursor_position(13,2)
                lcd.write(internet_poller.status)
            time.sleep(1)
            
    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        print "Shutting it down\n"
        gpsp.running = False
        gpsp.join()

    print "All Done.  Exiting"