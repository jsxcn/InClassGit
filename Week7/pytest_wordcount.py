import pytest
import wordcount

def wordcount_passing_cases():
    assert wordcount.wordcount('hello') == 5
    assert wordcount.wordcount('cs') == 2
