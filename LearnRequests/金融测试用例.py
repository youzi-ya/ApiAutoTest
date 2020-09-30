import requests

proxy={
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
  }
#注册
#投资人注册
url="http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=15210062333&pwd=111111111&regname=tz"
r=requests.get(url,proxies=proxy)
print(r.text)
#借款人注册
url1="http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=15529270306&pwd=111111111&regname=jk"
r=requests.get(url1,proxies=proxy)
print(r.text)
#获取用户列表
url2="http://192.168.150.222:8081/futureloan/mvc/api/member/list"
r=requests.get(url2,proxies=proxy)
print(r.text)

#投资人登录
url3="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu={"mobilephone":"15210062333","pwd":"111111111"}
r=requests.post(url3,data=canshu,proxies=proxy)
print(r.text)

#投资人充值
url4="http://192.168.150.222:8081/futureloan/mvc/api/member/recharge"
canshu1={"mobilephone":"15210062333","amount":"100000"}
r=requests.post(url4,data=canshu1,proxies=proxy)
print(r.text)

#借款人登录
url5="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu2={"mobilephone":"15529270306","pwd":"111111111"}
r=requests.post(url5,data=canshu2,proxies=proxy)
print(r.text)

#借款人提交借款申请材料，平台加贷款项目
url6="http://192.168.150.222:8081/futureloan/mvc/api/loan/add"
canshu3={"memberId":"  ","title":"借钱","amount":"50000","loanRate":"20.00",
         "loanTerm":"6","loanDateType":"0","repaymemtWay":"4","biddingDays":"7"}
r=requests.post(url6,data=canshu3,proxies=proxy)
print(r.text)

#获取标列表
url7="http://192.168.150.222:8081/futureloan/mvc/api/loan/getLoanList"
r=requests.post(url7,proxies=proxy)
print(r.text)

#平台人员审核1-运营人员审核（初审）
url8="http://192.168.150.222:8081/futureloan/mvc/api/loan/audit"
canshu4={"id":" ","status":"2"}
r=requests.post(url8,data=canshu4,proxies=proxy)
print(r.text)

#平台人员审核2-运营主管审核（复审）
canshu5={"id":" ","status":"3"}
r=requests.post(url8,data=canshu5,proxies=proxy)
print(r.text)

#平台人员审核3-运营总监审核（投标中状态）
canshu6={"id":" ","status":"4"}
r=requests.post(url8,data=canshu6,proxies=proxy)
print(r.text)

#投资人投标
url9="http://192.168.150.222:8081/futureloan/mvc/api/member/bidLoan"
canshu7={"memberId":"  ","password":"111111111","loanId":"  ","amount":"50000"}
r=requests.post(url9,data=canshu7,proxies=proxy)
print(r.text)

#投资人获取投资记录
url11="http://192.168.150.222:8081/futureloan/mvc/api/invest/getInvestsByMemberId"
canshu8={"memberId":"  "}
r=requests.post(url11,data=canshu8,proxies=proxy)
print(r.text)

#获取标的所有投资记录
url12="http://192.168.150.222:8081/futureloan/mvc/api/invest/getInvestsByLoanId"
canshu9={"loanId":"  "}
r=requests.post(url12,data=canshu9,proxies=proxy)
print(r.text)

#生成借款人回款计划
url13="http://192.168.150.222:8081/futureloan/mvc/api/loan/generateRepayments"
canshu10={"id":"  "}
r=requests.post(url13,data=canshu10,proxies=proxy)
print(r.text)
