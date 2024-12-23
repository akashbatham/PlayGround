import pytest


@pytest.mark.smoke
def test_first():
    print("First Program")


@pytest.mark.skip
def test_skipMethod():
    print("Skip Method")

@pytest.fixture()
def setup():
    print("I'm setup") #Any statement before YIELD is executed first in pytest
    yield #any statement after yield are tested are after all the other tests are completed
    print("After Yield statement")

def test_fixtureDemo(setup):
    print("I'm fixture method")
