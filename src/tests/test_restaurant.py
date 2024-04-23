"""
Unit tests for the methods of the Restaurant class.
"""

import unittest
from restaurant.restaurant import Restaurant

OPENING_TIME = 9
CLOSING_TIME = 22
CAPACITY = 5
BOOKINGS = [
    {
        'from': 10,
        'to': 14,
        'numPeople': 3
    },
    {
        'from': 11,
        'to': 13,
        'numPeople': 2
    },
    {
        'from': 13.5,
        'to': 15,
        'numPeople': 1
    },
    {
        'from': 16,
        'to': 20,
        'numPeople': 2
    }
]

RESTAURANT_PARAMETERS = (OPENING_TIME, CLOSING_TIME, CAPACITY)


class TestAvailableTimes(unittest.TestCase):
    """Tests for the available_times_for_reservation() method of the Restaurant class.
    
    test_X_guests() tests the method by computing the available times for a reservation
    of X guests and compares it with the expected result."""
    @classmethod
    def setUpClass(cls):
        cls.restaurant = Restaurant(*RESTAURANT_PARAMETERS)
        cls.restaurant.add_bookings_from_jsons_list(BOOKINGS)

    def test_0_guests(self):
        self.assertEqual(self.restaurant.available_times_for_reservation(0), [(9, 22)])

    def test_1_guest(self):
        self.assertEqual(self.restaurant.available_times_for_reservation(1), [(9, 11), (13, 22)])

    def test_2_guests(self):
        self.assertEqual(self.restaurant.available_times_for_reservation(2), [(9, 11), (13, 13.5), (14, 22)])

    def test_3_guests(self):
        self.assertEqual(self.restaurant.available_times_for_reservation(3), [(9, 10), (14, 22)])

    def test_4_guests(self):
        self.assertEqual(self.restaurant.available_times_for_reservation(4), [(9, 10), (14, 16), (20, 22)])

    def test_5_guests(self):
        self.assertEqual(self.restaurant.available_times_for_reservation(5), [(9, 10), (15, 16), (20, 22)])

    def test_more_guests_than_capacity(self):
        self.assertEqual(self.restaurant.available_times_for_reservation(6), [])

    @classmethod
    def tearDownClass(cls):
        del cls.restaurant


if __name__ == '__main__':
    unittest.main()