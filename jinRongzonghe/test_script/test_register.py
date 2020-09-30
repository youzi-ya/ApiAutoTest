'''
注册接口的脚本
'''

#pytest fixture 参数化的功能
#参数读进来

import pytest

from jinRongzonghe.baw.DbOp import DbOp
from jinRongzonghe.caw.DataRead import DataRead
from jinRongzonghe.baw.Member import Member
from jinRongzonghe.caw.Assert import Assert
#list 多组测试数据
@pytest.fixture(params=DataRead().read_yaml(r"data_case\register_fail.yaml"))
def fail_data(request):
    return request.param

@pytest.fixture(params=DataRead().read_yaml(r"data_case\register_success.yaml"))
def success_data(request):
    return request.param

@pytest.fixture(params=DataRead().read_yaml(r"data_case\register_repeat.yaml"))
def repeat_data(request):
    return request.param

#注册失败的逻辑
def test_reginster_fail(fail_data,url,base_requests):
    print(f"注册失败的用例，测试数据为:{fail_data}")
    r=Member().register(url,base_requests,fail_data['data'])
    #print(r.text)
    # assert str(fail_data['expect']['msg'])==str(r.json()['msg'])
    # assert str(fail_data['expect']['code']) == str( r.json()['code'])
    # assert str(fail_data['expect']['status']) ==str( r.json()['status'])
    Assert().equal(fail_data['expect'],r.json(),"msg,status,code")


#注册成功的逻辑
def  test_register_success(success_data,url,db,base_requests):
    print(f"注册成功的用例，测试数据为:{success_data}")
    #环境初始化
    DbOp().delete_user(db, success_data['data']['mobilephone'])
    r = Member().register(url, base_requests,success_data['data'])
    # print(r.text)

    # assert str(success_data['expect']['msg'] )== str(r.json()['msg'])
    # assert str(success_data['expect']['code']) ==str( r.json()['code'])
    # assert str(success_data['expect']['status']) ==str( r.json()['status'])
    Assert().equal(success_data['expect'], r.json(), "msg,status,code")

    #清理环境
    DbOp().delete_user(db,success_data['data']['mobilephone'])

#重复注册的逻辑
def  test_register_repeat(repeat_data,url,db,base_requests):
    print(f"重复注册的用例，测试数据为:{repeat_data}")
    r = Member().register(url, base_requests, repeat_data['data'])
    print(r.text)

