import unittest
import leap_year

class testCaseLeapYear(unittest.TestCase):
    def test_leapyear_1(self):
        self.assertEqual(leap_year.leapyear(2900), 0) #divisible by 4 and 100 should F

    def test_leapyear_2(self):
        self.assertEqual(leap_year.leapyear(1996), 1)

    def test_leapyear_1(self):
        self.assertEqual(leap_year.leapyear(0), -1)
