"""
======================================================================
Pinterest Mexico - Software Engineering Interview (Round 1)
======================================================================
>> Candidate:       Johann Gordillo
>> Interview Date:  04/18/2024
======================================================================
"""

import unittest
from tests.test_restaurant import TestAvailableTimes


def main() -> None:
    print("Running the unit tests...\n")
    runner = unittest.TextTestRunner(verbosity=0)
    suite = unittest.TestSuite([unittest.TestLoader().loadTestsFromTestCase(TestAvailableTimes)])
    runner.run(suite)


if __name__ == '__main__':
    main()
