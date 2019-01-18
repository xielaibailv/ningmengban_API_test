from urllib.request import Request,urlopen
import requests

# 作业：完成其中注册，登录，充值接口的调用

# 注册接口地址
# register = 'http://47.107.168.87:8080/futureloan/mvc/api/member/register'
# 登录接口地址
# login  = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
# 充值接口地址
# recharge = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'


# 注册接口get/post调用
# r1= requests.get('http://47.107.168.87:8080/futureloan/mvc/api/member/register',params={'mobilephone': 18600000000,'regname': '39kk','pwd': 123456})
# print(r1.text)
#
# r2 = requests.post('http://47.107.168.87:8080/futureloan/mvc/api/member/register',data={'mobilephone': 18612345678,'regname': '39kk','pwd': 123456})
# print(r2.text)

# 登录接口get/post调用
login_url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
headers = {'user-Agent': 'Mozilla/5.0'}
params1 = {'mobilephone': 18600000000, 'pwd': 1234567}
params2 = {'mobilephone': 18612345678, 'pwd': 123456}
r3 = requests.get(login_url, headers=headers, params=params1)
print('响应码：', r3.status_code)
print('响应信息：', r3.text)

r4 = requests.post(login_url,data=params2)
print('响应码：', r4.status_code)
print('响应信息：', r4.text)
print('cookie信息：', r4.cookies)

cookie = r4.cookies

# 充值接口get/post调用
recharge_url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
params3 = {'mobilephone': 18612345678, 'amount': 100000}
r5 = requests.get(recharge_url, headers=headers, params=params3,cookies=cookie)
print(r5.text)

r6 = requests.post(recharge_url, headers=headers, params=params3,cookies=cookie)
print(r5.text)
print('响应信息里的响应码：', r5.json()['status'])