#! /usr/bin/python
import threading
import os
import time
import pdb
from zone_calculator import ZoneCalculator

class ZonePoller(threading.Thread):
    def __init__(self, gps_poller):
        threading.Thread.__init__(self)
        self.gps_poller = gps_poller
        self.zone_calculator = ZoneCalculator('saint_louis.json')
        self.current_zone = None

    def run(self):
        latitude = self.gps_poller.gpsd.fix.latitude
        longitude = self.gps_poller.gpsd.fix.longitude
        self.current_zone = self.zone_calculator.current_zone(latitude, longitude)
        time.sleep(1)

