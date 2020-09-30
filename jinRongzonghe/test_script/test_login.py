'''
登录接口的脚本
'''
import pytest

from jinRongzonghe.baw.DbOp import DbOp
from jinRongzonghe.caw.DataRead import DataRead
from jinRongzonghe.baw.Member import Member
from jinRongzonghe.caw.Assert import Assert
#list 多组测试数据
# @pytest.fixture(params=DataRead().read_yaml(r"data_case\login_setup.yaml"))
# def setup_data(request):
#     return request.param

@pytest.fixture(params=DataRead().read_yaml(r"data_case\login_data.yaml"))
def login_data(request):
    return request.param

# @pytest.fixture()
# def register(setup_data,url,db,base_requests):
#     r = Member().register(url, base_requests, setup_data['data'])
#      #注册用户
#     yield
#     # 删除注册用户
#     DbOp().delete_user(db, setup_data['data']['mobilephone'])


#登录的逻辑
def test_login(url,base_requests,register,login_data):
    # print(f"登录的用例，测试数据为:{login_data}")
    r=Member().login(url,base_requests,login_data['data'])
    Assert().equal(login_data['expect'],r.json(),"msg,status,code")


