"""
Auxiliary functions to manage time slots.
"""

from typing import List, Tuple

type TimeSlot = Tuple[float, float]


def merged_time_slots(time_slots: List[TimeSlot]) -> List[TimeSlot]:
    """Merges the intersecting time slots of a list."""
    if len(time_slots) < 2:
        return time_slots
    
    time_slots.sort(reverse=True)
    
    merged_slots = []
    while len(time_slots) > 1:
        slot1 = time_slots.pop()
        slot2 = time_slots.pop()

        if time_slots_intersect(slot1, slot2):
            time_slots.append(merge_two_time_slots(slot1, slot2))
        else:
            # slot1 doesn't intersect with other time slots, so we add it to the answer.
            # We keep slot2, because it still can intersect with other time slots.
            merged_slots.append(slot1)
            time_slots.append(slot2)
    merged_slots.append(time_slots.pop())

    return merged_slots


def merge_two_time_slots(slot1: TimeSlot, slot2: TimeSlot) -> List[TimeSlot]:
    """Merges two time slots into a single one."""
    return (min(slot1[0], slot2[0]), max(slot1[1], slot2[1]))


def time_slots_intersect(slot1: TimeSlot, slot2: TimeSlot) -> bool:
    """Returns True if two time slots intersect with each other. False otherwise."""
    return slot1[1] >= slot2[0]
