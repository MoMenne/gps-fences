#! /usr/bin/python
import threading
import os 

class InternetPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
  
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

