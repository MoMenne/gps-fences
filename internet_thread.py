#! /usr/bin/python
import threading
import os 
import time
import pdb
import socket
# this makes it easy to find the local IP
from netifaces import interfaces, ifaddresses, AF_INET

class InternetPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.status = None
        self.eth0_address = None

    def run(self):
        # update the ip address
        self.eth0_address = [i['addr'] for i in ifaddresses("eth0").setdefault(AF_INET, [{'addr':'No IP addr'}] )]

        # check if internet connection
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("google.com",80))
            s.close()
            self.status = " up"
        except:
            pdb.set_trace()
            self.status = "dwn"
        time.sleep(1)

