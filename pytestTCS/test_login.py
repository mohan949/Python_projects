import pytest
import random

@pytest.mark.xfail
def testLogin():
    print('login successful')

@pytest.mark.regression
def testLogOff():
    print('logOff Succesfull')

@pytest.mark.sanity
def testCalculator():
    try:
        assert 2+2 == 4
    except Exception as e:
        print('error ---->',e)
    


