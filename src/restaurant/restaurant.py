"""
Restaurant model with the needed business logic to manage the restaurant's information
and retrieve its available times for clients to make a reservation.
"""

from utils.time_slots_utils import merged_time_slots

from typing import Dict, Union, List, Tuple

type TimeSlot = Tuple[float, float]


class Restaurant(object):
    """Class for modelling a restaurant."""

    class _Booking(object):
        """Class for modelling a booking.
        
        A booking is a reserved time in a restaurant, for a given number of people, from a
        starting hour to a finishing hour."""
        def __init__(self, from_time: float, to_time: float, num_people: int) -> None:
            self.from_time = from_time
            self.to_time = to_time
            self.num_people = num_people

    def __init__(self, opening_time: float, closing_time: float, capacity: int) -> None:
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.capacity = capacity
        self.bookings = []

    def add_booking(self, booking: _Booking) -> None:
        """Adds a booking to the bookings list."""
        self.bookings.append(booking)

    def add_bookings_from_jsons_list(self, jsons_list: Dict[str, Union[float, float, int]]) -> None:
        """Adds one or more bookings to the current bookings list from a list of jsons,
        each of those representing a new booking."""
        for json in jsons_list:
            self.add_booking(self._Booking(json['from'], json['to'], json['numPeople']))

    def available_times_for_reservation(self, num_people: int) -> List[TimeSlot]:
        """Obtains a list of the time lapses available for reservation. 
        
        A time lapse is represented by a tuple of the form (start, end), where start and end
        are decimal numbers, both representing an hour in the 24h format."""
        if num_people > self.capacity:
            return []
        
        num_bookings = len(self.bookings)
        if num_bookings == 0:
            return [(self.opening_time, self.closing_time)]

        starts_of_bookings = []
        ends_of_bookings = []
        for booking in self.bookings:
            starts_of_bookings.append((booking.from_time, booking.num_people))
            ends_of_bookings.append((booking.to_time, booking.num_people))
        starts_of_bookings.sort()
        ends_of_bookings.sort()

        index_starts_of_bookings = 0
        index_ends_of_bookings = 0

        curr_capacity = self.capacity
        left = self.opening_time

        # There is a free time slot from the opening time of the restaurant to the 
        # start of the first reservation.
        available_slots = [(self.opening_time, starts_of_bookings[0][0])]

        while index_starts_of_bookings < num_bookings:
            start = starts_of_bookings[index_starts_of_bookings][0]
            start_clients = starts_of_bookings[index_starts_of_bookings][1]

            end = ends_of_bookings[index_ends_of_bookings][0]
            end_clients = ends_of_bookings[index_ends_of_bookings][1]

            if start < end:
                if num_people <= curr_capacity:
                    available_slots.append((left, start))
                left = start
                curr_capacity -= start_clients
                index_starts_of_bookings += 1

            else:
                if num_people <= curr_capacity:
                    available_slots.append((left, end))
                left = end
                curr_capacity += end_clients
                index_ends_of_bookings += 1

        if num_people <= curr_capacity:
                available_slots.append((left, self.closing_time))

        # There is a free time slot from the end of the last reservation to the
        # closing time of the restaurant
        available_slots.append((ends_of_bookings[len(ends_of_bookings) - 1][0], self.closing_time))
        
        return merged_time_slots(available_slots)
