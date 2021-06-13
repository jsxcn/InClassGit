import unittest
import leapYear

class testCaseLeapYear(unittest.TestCase):
    def test_leapyear_1(self):
        self.assertEqual(leapYear.leapyear(2900), 0)
    def test_leapyear_2(self):
        self.assertEqual(leapYear.leapyear(1996), 1)
    def test_leapyear_3(self):
        self.assertEqual(leapYear.leapyear(1400), 0)


if __name__ == '__main__':
    unittest.main()
