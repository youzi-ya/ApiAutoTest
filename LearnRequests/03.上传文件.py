'''
个人中心->上传头像。
'''

import requests

# 上传一个图片文件
url = "http://www.httpbin.org/post"
file_path = "d:/test.png"
with open(file_path, mode='rb') as f:
    # 二元组：'name': file-tuple， file-tuple为('filename', fileobj)
    # file = {"test.png": (file_path, f)}
    # 三元组：'name': file-tuple， file-tuple为('filename', fileobj, 'content_type')
    # content_type 指的是MIME类型
    file = {"test.png": (file_path, f, "image/png")}
    r = requests.post(url, files=file)
    print(r.text)

# 上传多个文件
url = "http://www.httpbin.org/post"
file_path1 = "d:/test.png"
file_path2 = "d:/test.txt"
with open(file_path1, mode='rb') as f1:
    with open(file_path2, mode='r', encoding='utf-8') as f2:
        files = {"test.png": (file_path1, f1, "image/png"),
                 "test.txt": (file_path2, f2, "text/plain")}
        r = requests.post(url, files=files)
        print(r.text)

# 使用data上传文件，一次只能上传一个文件
file_path2 = "d:/test.txt"
with open(file_path2, mode='rb') as ff:
    r = requests.post(url, data=ff)
    print(r.text)
