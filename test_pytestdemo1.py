import pytest


# This is a setup once every test case
@pytest.yield_fixture()
def setup():
    print("once before every method")
    yield
    print("this is a second time after yield")


# every method need to be called inside the function
def tests_method1(setup):
    print("this is method 1")


# every method need to be called inside the function
def test_method2(setup):
    print("this is a method 2")
