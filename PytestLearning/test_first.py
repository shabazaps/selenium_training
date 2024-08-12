import pytest


def test_first():
    print("Hello, world!")


@pytest.mark.smoke
@pytest.mark.xfail
def test_chrome():
    print("Hello world")


@pytest.mark.smoke
@pytest.mark.skip
def test_safari2():
    a = "Shabaz"
    b = "Shabaz"
    assert a == b, " Test Failed"
