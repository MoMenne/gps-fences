#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0
 
import os
from gps import *
from time import *
import time
import threading
import dothat.backlight as backlight
import dothat.lcd as lcd
 
gpsd = None #seting the global variable
 
os.system('clear') #clear the terminal (optional)

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while self.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

class InternetPoller(threading.Thread):
  def __init__(self):
    threading.Thread__init__(self)
  
  def run(self):
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

 
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  show_gps = False   # show GPS by default 
  show_ip  = True 

  try:
    gpsp.start() # start it up
    while True:
      #It may take a second or two to get good data
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
 
      os.system('clear')
 
      print
      print ' GPS reading'
      print '----------------------------------------'
      print 'latitude    ' , gpsd.fix.latitude
      print 'longitude   ' , gpsd.fix.longitude
      print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
      print 'altitude (m)' , gpsd.fix.altitude
      print 'eps         ' , gpsd.fix.eps
      print 'epx         ' , gpsd.fix.epx
      print 'epv         ' , gpsd.fix.epv
      print 'ept         ' , gpsd.fix.ept
      print 'speed (m/s) ' , gpsd.fix.speed
      print 'climb       ' , gpsd.fix.climb
      print 'track       ' , gpsd.fix.track
      print 'mode        ' , gpsd.fix.mode
      print
      print 'sats        ' , gpsd.satellites

      if show_gps 
        lcd.set_cursor_position(0,0)
        lcd.write("heading " + "%.2f" % gpsd.fix.track )
        lcd.set_cursor_position(0,1)
        lcd.write("lat  " + "%.5f" % gpsd.fix.latitude )
        lcd.set_cursor_position(0,2)
        lcd.write("long " + "%.5f" % gpsd.fix.longitude)
 
      time.sleep(5) #set to whatever
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
