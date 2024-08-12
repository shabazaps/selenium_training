import pytest


def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


@pytest.mark.skip
def test_fixtureDemo(setup):
    print("I will execute steps in fixture")
