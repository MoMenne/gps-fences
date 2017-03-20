#!/usr/bin/env python
import time
import socket

import dothat.backlight as backlight
import dothat.lcd as lcd

	
# this makes it easy to find the local IP
from netifaces import interfaces, ifaddresses, AF_INET

print("""
	Running GPS via the Raspberry Pi
""")

backlight.rgb(255,0,255)
lcd.write("ESS GPS")
backlight.graph_off()
lcd.clear()


# determine the ip address of the pi
for ifaceName in interfaces():
	addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
	print '%s: %s' % (ifaceName, ', '.join(addresses))

while True:
	# update the ip address
	eth0_address = [i['addr'] for i in ifaddresses("eth0").setdefault(AF_INET, [{'addr':'No IP addr'}] )]

	# check if internet connection
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("google.com",80))
		s.close()
		status = " up"
	except:
		status = "dwn"
	lcd.clear()
	lcd.set_cursor_position(0,2)
	lcd.write(eth0_address[0])
	lcd.set_cursor_position(13,2)
	lcd.write(status)

	print "update ip " + eth0_address[0] + status

	time.sleep(1)
