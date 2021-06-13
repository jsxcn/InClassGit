import pytest
import leapYear

def testCaseLeapYears():
    assert leapYear.leapyear(400) == 1
    assert leapYear.leapyear(1996) == 1
    assert leapYear.leapyear(1900) == 0
