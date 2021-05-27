import unittest
import average

class testCaseAvg(unittest.TestCase):
#normal 
    def test_average_1(self):
        self.assertEqual(average.avg(5,5,5,5,5), 4)


#check for empty list
    def test_average_2(self):
    self.assertTrue(avg)

#check for when list is divided by zero
    def test_average_3(self):
        self.assertEqual(average.avg(5,5,5,5,0), 0)

if __name__ == "__main__":
    unittest.main()
