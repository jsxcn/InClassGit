import pytest
import palindrome

def palindrome_passing_cases():
    assert palindrome.palindrome('hello') == False
    assert palindrome.palindrome('otto') == True
