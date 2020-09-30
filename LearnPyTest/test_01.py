'''
测试文件以test_开头
测试函数/方法以test_开头
'''


def add(a, b):
    try:
        return a + b
    except Exception as e:
        return str(e).strip()


# 为上面的函数设计测试用例，每个用例用test_开头
# 整数的加法
def test_case01():
    ret = add(1, 2)  # 调用上面的函数
    assert ret == 3  # 校验结果


# 浮点数的加法
def test_case02():
    ret = add(0.1, 0.2)
    assert ret == 0.3


# 列表的加法
def test_case03():
    ret = add([1, 2], [3, 4])
    assert ret == [1, 2, 3, 4]


# 整数和字符串的加法
def test_case04():
    ret = add(1, "1")
    assert ret == "unsupported operand type(s) for +: 'int' and 'str'"
