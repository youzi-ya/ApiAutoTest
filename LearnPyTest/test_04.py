'''
mark标记
1. 实现参数化
2. 跳过
'''

import pytest
import requests

url = "http://192.168.150.52:8089/futureloan/mvc/api/member/register"

# 从yaml文件中读取，从csv文件中读取
# 测试数据
case_data = [("18091234567", "123456", "投资人", "手机号码已被注册", "20110", 0),
             ("180", "8888", "借款人", "密码长度必须为6~18", "20108", 0)]


@pytest.mark.parametrize("mobile, pwd, regname,msg, code, status", case_data)
# 测试逻辑
def test_register(mobile, pwd, regname, msg, code, status):
    print(f"测试注册功能：{mobile}, {pwd}, {regname}")
    param = {"mobilephone": mobile, "pwd": pwd, "regname": regname}
    ret = requests.post(url, data=param)
    assert ret.json()["msg"] == msg
    assert ret.json()["code"] == code
    assert ret.json()["status"] == status


withdraw_data = [("18091234567", "10")]


# @pytest.mark.skip("该接口未实现，本版本暂不执行")
@pytest.mark.skipif(1 == 1, reason="前面表达式为true时，跳过；表达式为false时，不跳过")
@pytest.mark.parametrize("mobile, amount", withdraw_data)
def test_withdraw(mobile, amount):
    url = "http://192.168.150.52:8089/futureloan/mvc/api/member/withdraw"  # recharge 充值
    print(f"测试取款的功能：{mobile}, {amount}")
    param = {"mobilephone": mobile, "amount": amount}
    ret = requests.post(url, data=param)
    assert ret.json()['msg'] != "服务器异常"
