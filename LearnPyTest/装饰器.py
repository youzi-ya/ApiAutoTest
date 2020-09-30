'''
装饰器：运行中增加功能的一种方式
'''

'''
已经写好了一些测试用例，后面维护代码时，想增强这些用例的功能，比如增加日志。又不想改test_case1、test_case2的代码。
将写日志的功能定义成一个装饰器。装饰器是拿函数作为参数。
'''


def log(func):
    # *args, **kw的目：func可以有任意个参数
    def wrapper(*args, **kw):
        # 每个函数有一个__name__属性，返回函数的名字
        print(f"in 函数：{func.__name__}")
        func(*args, **kw)
        print(f"out 函数：{func.__name__}")

    return wrapper



def test_case1():
    print("in 函数：test_case1")
    print("用例1")
    print("out 函数：test_case1")

@log
def test_case2():
    print("用例2")

@log
def test_case3():
    print("用例3")
