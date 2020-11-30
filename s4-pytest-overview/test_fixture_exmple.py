import pytest

@pytest.fixture()
def setup():
    print("\nSetup")

@pytest.fixture(autouse=True)
def setup2():
    print("\nSetup2")

#use setup as a parameter
def test1(setup):
    print("\nExecuting test1!")
    assert True

#usefixtures decorator
@pytest.mark.usefixtures("setup")
def test2():
    print("\nExecuting test2!")
    assert True