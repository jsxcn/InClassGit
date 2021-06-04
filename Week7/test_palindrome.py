import unittest
import palindrome

class testPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome.palindrome("hello"), False)
    def test_palindrome(self):
        self.assertEqual(palindrome.palindrome("otto"), True)
