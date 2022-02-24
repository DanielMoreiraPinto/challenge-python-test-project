from unittest import TestCase
import pytest
from context import src
from ddt import ddt,data,unpack

from src import booking_controller

@ddt
class TestBookingController(TestCase):
    
    sut = booking_controller.BookingController()
    
    @data(("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)", 'Lakewood'),
            ("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)", 'Ridgewood'),
            ("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)", 'Ridgewood'))
    @unpack
    def test_assist_booking_returns_cheapest_hotel(self, input, expected):
        result = self.sut.assist_booking(input)
        self.assertEqual(result, expected)