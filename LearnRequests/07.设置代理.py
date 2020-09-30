'''
1.爬虫之类的场景，避免服务器认为是攻击，将IP屏蔽掉
2.代理抓包，定位问题
'''

import requests

proxy = {
    # http协议，使用"http://127.0.0.1:8888"代理，8888与fiddler的端口号一致。
    "http": "http://127.0.0.1:8888",
    # https协议，使用"http://127.0.0.1:8888"代理，8888与fiddler的端口号一致。
    "https": "http://127.0.0.1:8888"
}
r = requests.get("http://www.baidu.com/s?wd=123123123", proxies=proxy)
# print(r.text)
# requests.put()
# requests.delete()

r= requests.get("http://192.168.150.222:8081/futureloan/mvc/api/loan/getLoanList")
print(r.text)
