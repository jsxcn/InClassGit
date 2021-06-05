import unittest
import leap_year

class testCaseAdd(unittest.TestCase):
    def test_leapyear_1(self):
        self.assertEqual(leap_year.leapyear(1600), 1)

    def test_leapyear_2(self):
        self.assertEqual(leap_year.leapyear(21000), 0)

    def test_leapyear_1(self):
        self.assertEqual(leap_year.leapyear(0), -1)
