import unittest
import FizzBuzz

class testFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(FizzBuzz.FizzBuzz(67), 67)

    def test_fizzbuzz_2(self):
        self.assertEqual(FizzBuzz.FizzBuzz(65), 'Buzz')

    def test_fizzbuzz_3(self):
        self.assertEqual(FizzBuzz.FizzBuzz(60), 'FizzBuzz')



if __name__ == "__main__":
    unittest.main()
