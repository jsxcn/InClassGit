import unittest
import activitycalc

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(activitycalc.add(10,5), 15) #this pass: .

    def test_add_2(self):
        self.assertEqual(activitycalc.add(10,15), 4) # this failed: F

    def test_subract(self):
        self.assertEqual(activitycalc.subtract(10,5), 5)

    def test_subract_2(self):
        self.assertEqual(activitycalc.subtract(20,5), 15)

    def test_multiple(self):
        self.assertEqual(activitycalc.multiple(5,5), 25)

    def test_multiple_2(self):
        self.assertEqual(activitycalc.multiple(5,5), 15)

    def test_divide(self):
        self.assertEqual(activitycalc.divide(10,5), 2)

    def test_divide_2(self):
        self.assertEqual(activitycalc.divide(10,5), 0)

if __name__ == "__main__":
    unittest.main()
