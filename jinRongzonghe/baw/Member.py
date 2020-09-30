'''
业务am：按模块划分
business action word

'''
REGISTER="futureloan/mvc/api/member/register"
LOGIN="futureloan/mvc/api/member/login"
class Member:
    def register(self,url,base_requests,data):
        '''
        用户注册的接口
        :param url:   环境信息  http://host：port/
        :param base_requests:
        :param data:  数据
        :return:   响应信息
        '''
        real_url=url+REGISTER

        r=base_requests.post(real_url,data=data)
        return r

    def login(self,url,base_requests,data):
        '''

        :param url:
        :param base_requests:
        :param data:
        :return:
        '''
        real_url = url + LOGIN

        r = base_requests.post(real_url, data=data)
        return r


if __name__ == '__main__':
    from jinRongzonghe.caw.BaseRequests  import BaseRequests
    r=Member().register("http://192.168.150.222:8081/",BaseRequests(),{"mobilephone":"13290815517"})
    print(r.text)

    r = Member().login("http://192.168.150.222:8081/", BaseRequests(), {"mobilephone": "13290815517"})
    print(r.text)