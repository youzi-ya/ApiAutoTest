'''
发送get请求：
1.get不带参数
2.get请求带参数
'''

import requests  # 导入包

url = "http://www.baidu.com"
r = requests.get(url)  # 发送get请求，使用变量r接收响应
print(r.text)  # 文本类型的
print(r.status_code)  # 状态码  200
print(r.reason)  # 状态原因  OK
print("r.cookies=", r.cookies)  # 响应信息的cookies
print(r.headers)  # 响应的头部信息
print(r.raw)  # 原始格式的  <urllib3.response.HTTPResponse object at 0x00000210A2529390>
# print(r.)
# print(r.raw.read(10))


# 金融项目注册
# 方法1：参数拼接在URL的后面，? 号后面是参数，参数之间用&拼接。 参数=值
url = "http://192.168.150.52:8089/futureloan/mvc/api/member/register?mobilephone=18091234567&pwd=123456&regname=auto"
r = requests.get(url)
print(r.text)  # {"status":0,"code":"20110","data":null,"msg":"手机号码已被注册"}
print(r.json())  # {'status': 0, 'code': '20110', 'data': None, 'msg': '手机号码已被注册'}
print(type(r.json()))  # <class 'dict'>

# 方法2：使用params传参
url = "http://192.168.150.52:8089/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "18091234567", "pwd": "123456", "regname": "test"}
r = requests.get(url, params=canshu)
print(r.json())

# httpbin，一个测试网站，有get/post等接口，参数任意构造，服务器将发送的请求转成json格式的返回
r = requests.get("http://www.httpbin.org/get?username=123&pwd=456&email=123456@qq.com")
print(r.text)

url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=18091831234"
ret = requests.get(url)
print(ret.text)

url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
params = {"tel": "18091831234"}
ret = requests.get(url, params=params)
print(ret.text)
# print(ret.json())


# 发送的请求带请求头
# 设置User-Agent，伪装成浏览器发送的请求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
r = requests.get("http://www.httpbin.org/get?username=123&pwd=456&email=123456@qq.com", headers=headers)
print(r.text)

# 既带参数，又带请求头
# requests.get(url, params=, headers=)
