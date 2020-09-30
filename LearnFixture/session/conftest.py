'''
conftest.py：存放session级别的fixture的文件，pytest根据文件名字查找
'''
import pytest


@pytest.fixture(scope='session')
def login():
    print("登录")
    yield
    print("退出登录")

@pytest.fixture(scope='session')
def db():
    print("连接数据库")
    yield
    print("断开数据库连接")
