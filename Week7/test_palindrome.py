import unittest
import palindrome

class testPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome.palindrome("hello"), False)
    def test_palindrome_2(self):
        self.assertEqual(palindrome.palindrome("otto"), True)

if __name__ == '__main__':
    unittest.main()
