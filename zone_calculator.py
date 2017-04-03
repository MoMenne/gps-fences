#! /usr/bin/python
import pdb
import json
import logging
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class ZoneCalculator:
    def __init__(self, test_file):
        print "creating zone calculator"
        self.zones = []
        with open("data/{}".format(test_file)) as data_file:
            self.data = json.load(data_file)

    def about(self, some_float, some_other_float):
        return abs(some_float - some_other_float) <= .0001

    def current_zone(self, latitude, longitude):
        point = Point(latitude, longitude)
        for zone in self.data:
            polygon = Polygon(map(lambda x: [x['lat'], x['long']], zone['points']))
            if polygon.contains(point):
                logging.debug("In {}".format(zone['zone']))
                return zone['zone']

        return "No Zone"
