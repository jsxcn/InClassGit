import pytest
import unittest
import wordcount

def wordcount_passing_cases():
    assert wordcount.wordcount('hello') == 1
    assert wordcount.wordcount('hello world') == 2
    assert wordcount.wordcount('like an echo in the forest') == 7
