'''
脚本层的公共方法
'''

import pytest

#读取环境文件，获取url
from jinRongzonghe.baw.DbOp import DbOp
from jinRongzonghe.baw.Member import Member
from jinRongzonghe.caw.Assert import Assert
from jinRongzonghe.caw.BaseRequests import BaseRequests
from jinRongzonghe.caw.DataRead import DataRead

ENVPATH =r'data_env\env.ini'

#读取环境文件，获取url
@pytest.fixture(scope="session")
def url():
    return DataRead().read_ini(ENVPATH ,'url')

#读取环境文件，获取db
@pytest.fixture(scope="session")
def db():
    return eval(DataRead().read_ini(ENVPATH ,'db'))


#BaseRequests实例化，整个执行过程实例化一次
@pytest.fixture(scope="session")
def base_requests():
    return BaseRequests()

@pytest.fixture(scope="session",params=DataRead().read_yaml(r"data_case\login_setup.yaml"))
def setup_data(request):
    return request.param

@pytest.fixture(scope="session")
def register(setup_data,url,db,base_requests):
    r = Member().register(url, base_requests, setup_data['data'])
    Assert().equal(setup_data['expect'], r.json(), "msg,status,code")
     #注册用户
    yield
    # 删除注册用户
    DbOp().delete_user(db, setup_data['data']['mobilephone'])