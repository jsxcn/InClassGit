import unittest
import reverseSen

class testreversesen(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverseSen.reverseStr("Hello this is a test"), "test a os this hello")
    def test_reverse_2(self):
        self.assertEqual(reverseSen.reverseStr("Hello world"), "world Hello")
    def test_reverset_3(self):
        self.assertEqual(reverseSen.reverseStr("Life goes on"), "on goes Life")


if __name__ == '__main__':
    unittest.main()
