import pytest


def test_safari():
    a= 4
    b =8
    assert a+4 == b,"Assertion failed"
@pytest.mark.smoke
def test_chrome():
    a= "Hello"
    b ="World"
    assert a == b,"Assertion failed"