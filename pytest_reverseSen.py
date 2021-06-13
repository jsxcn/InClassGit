import pytest
import reverseSen

def reverseSen_passing_cases():
    assert reverseSen.reverseStr('hello world') == 'world hello'
    assert reverseSen.reverseStr('what if monkey doesnt eat banana') == 'banana eat doesnt monkey if what'
    assert reverseSen.reverseStr('like an echo in the forest') == 'forest the in echo an like'
    assert reverseSen.reverseStr('one') == 'one'
