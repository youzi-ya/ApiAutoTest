'''
两种超时的场景：
1.接口耗时比较久，设置超时时间，避免还没有执行完，超时退出了。
2.接口性能，比如接口要求在500ms内执行完成。
'''

import requests

for i in range(100):
    try:
        url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=18091831234"
        ret = requests.get(url, timeout=0.5)
        print(ret.status_code)  # requests.exceptions.ConnectTimeout
    except Exception as e:
        print(e)
