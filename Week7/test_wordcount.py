import unittest
import wordcount

class testwordcount(unittest.TestCase):
    def test_wordcount(self):
        self.assertEqual(wordcount.wordcount("Hello"), 5)
    def test_wordcount_2(self):
        self.assertEqual(wordcount.wordcount("Listen"), 6)
    def test_wordcount_3(self):
        self.assertEqual(wordcount.wordcount("Listen"), 8)
