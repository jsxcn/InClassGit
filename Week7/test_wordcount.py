import unittest
import wordcount

class testwordcount(unittest.TestCase):
    def test_wordcount(self):
        self.assertEqual(wordcount.wordcount("Hello this is a test"), 5)
    def test_wordcount_2(self):
        self.assertEqual(wordcount.wordcount("Listen"), 1)
    def test_wordcount_3(self):
        self.assertEqual(wordcount.wordcount("Life goes on"), 3)


if __name__ == '__main__':
    unittest.main()
