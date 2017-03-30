#! /usr/bin/python
import threading
import pdb
from gps import *

class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.gpsd = gps(mode=WATCH_ENABLE)
        self.current_value = None
        self.running = True

    def run(self):
        while self.running:
            self.gpsd.next()

