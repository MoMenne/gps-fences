#! /usr/bin/python
import unittest
from zone_calculator import ZoneCalculator 

class TestZoneCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ZoneCalculator("test.json")

    def test_current_zone_returns_something(self):
        self.assertTrue(self.calculator.current_zone)

    def test_that_border_is_in_zone(self):
        self.assertEquals("Bermuda Triangle", self.calculator.current_zone(26, -79))

    def test_point_is_not_in_any_zone(self):
        self.assertEquals("No Zone", self.calculator.current_zone(100, 100))

    def test_that_current_zone_is_tilles_park(self):
        self.assertEquals("Tilles Park", self.calculator.current_zone(38.600368, -90.290021))


if __name__ == "__main__":
    unittest.main()
