# Pinterest Mexico - Software Engineering Interview 🇲🇽

Round 1 of the interview process for the Backend Engineer position in Pinterest Mexico.

I didn't pass the interview because I'm dumb, my code sucks and I get nervous sometimes :disappointed:, but it was a nice challenge :computer:

## Problem statement 📋

You're a restaurant manager who's job is to find the available time slots for seating *N* number of guest(s).

A restaurant has the following structure:
```
restaurant = {
    'opening_time': 9,
    'closing_time': 22,
    'capacity': 5,
    'bookings': [
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
}
```

Where *opening_time* and *closing_time* are the open time and the close time of the restaurant, respectively, and *capacity* is the maximum number of guests that can be inside the restaurant at the same time.

Implement an algorithm to find all the available time slots for seating a given number of guests.

Time slots will be represented by pairs of the form (start, end).

## Solution :pencil:

The main algorithm is implemented in the *available_times_for_reservation()* method of the Restaurant class.

```
class Restaurant():
  ...

  def available_times_for_reservation(self, num_people: int) -> List[TimeSlot]:
    ...
```

If *num_people* is bigger than the restaurant's capacity, there will not be available time slots, hence the resulting list will be empty.

Then, if there are no current bookings in the restaurant, the answer will be a list with the time slot (opening_time, closing_time).

If neither of those cases are true, we create the following two lists:

- **starts_of_bookings:** A list of tuples of the form (hour, guests) where *hour* is the starting time of a booking and *guests* is the number of guests in that reservation.
- **ends_of_bookings:** A list of tuples of the form (hour, guests) where *hour* is the ending time of a booking and *guests* is the same as above.

and we sort them.

In each iteration of the algorithm, we'll take the earliest time from one of the lists.

If the earliest time is in the *starts_of_bookings* list, we'll decrease the current capacity of the restaurant, according to the number of guests in that reservation.

Otherwise, if the earliest time is in the *ends_of_bookings* list, we'll increase the current capacity.

In both cases, if the current capacity is bigger or equal than *num_people*, we'll update the output list by adding a new available time slot to it.

Finally, we'll merge the resulting time slots and that will be the final answer. For example, a list of the form [(11, 16.5), (17, 19), (19, 23)] will be converted to [(11, 16.5), (17, 23)],
because the union of the (17, 19) and (19, 23) time slots is the (17, 23) time slot.

## Time Complexity :mag_right:

The time complexity of the algorithm is ***O(N log N)*** because of the sorting needed.

---
⌨️ with ❤️ by [Johann Gordillo](https://github.com/JohannGordillo) 😊
