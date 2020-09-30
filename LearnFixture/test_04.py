'''
fixture带返回值
'''
import pytest


@pytest.fixture()
def data():
    return {"username":"root", "pwd":"123456"}


def test_case01(data):
    print(f"{data}")
    print(f"{data['username']}")
    print(f"{data['pwd']}")