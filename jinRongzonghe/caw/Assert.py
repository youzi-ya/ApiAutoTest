'''
断言公共方法
'''

import pytest_check as check

class Assert:


    def equal(self,expect,response,key_str):
        '''

        :param expect:
        :param response:
        :param key_str:
        :return:
        '''
        try:
            keys=key_str.split(",")   #安逗号分隔开
            for key in keys:   #遍历每个key
                r=str(response[key] )  #根据key取value
                e=str(expect[key])
                check.equal(r,e)
                print(f"响应信息为:{response},预期结果为{expect},校验字段为{key},实际结果为{r},预期结果为{e},校验成功")
        except Exception as e:
            print(f"响应信息为:{response},预期结果为{expect},校验字段为{key},实际结果为{r},预期结果为{e},校验失败")