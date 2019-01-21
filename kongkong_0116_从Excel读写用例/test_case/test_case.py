import unittest
from ddt import ddt,data
import requests
from kongkong_0116_从Excel读写用例.conf_file.read_conf import ReadConf
from kongkong_0116_从Excel读写用例.test_data.do_excel import DoExcel
from kongkong_0116_从Excel读写用例.test_data.do_log import DoLog

# 从配置文件获取URL
conf_file = '../conf_file/conf.ini'
register_url = ReadConf(conf_file).get_value('URL', 'register_url')  # 注册
login_url = ReadConf(conf_file).get_value('URL', 'login_url')        # 登录
recharge_url = ReadConf(conf_file).get_value('URL', 'recharge_url')  # 充值
headers = eval(ReadConf(conf_file).get_value('HEAD', 'headers'))
method = ReadConf(conf_file).get_value('METHOD', 'method').upper()   # 请求方法

# 从excel获取测试用例
register = DoExcel('../test_data/test_data.xlsx', 'register')
login = DoExcel('../test_data/test_data.xlsx', 'login')
recharge = DoExcel('../test_data/test_data.xlsx', 'recharge')
register_cases = register.read_data()   # 注册数据
login_cases = login.read_data()         # 登录数据
recharge_cases = recharge.read_data()   # 充值数据

session = requests.session()  # 实例化session，所有用例执行使用同一个session

# 创建日志
my_log = DoLog()


@ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        pass

    # 测试注册接口
    @data(*register_cases)
    def test_register(self, register_case):
        my_log.info('注册接口：开始执行第{}条用例：{}!!!'.format(register_case.id, register_case.title))
        r = session.request(method=method, url=register_url, headers=headers, data=register_case.data)
        my_log.info(r.text)
        result = r.json()['status']
        try:
            self.assertEqual(register_case.expected, result)
            test_result = 'PASS'
        except AssertionError as e:
            test_result = 'FAILD'
            msg = '测试失败，失败原因：{}'.format(e)
            text = r.text
            my_log.error(msg)
            my_log.error(text)
            raise e
        finally:
            login.write_data(row=register_case.id + 1, column=7, value=result)
            login.write_data(row=register_case.id + 1, column=8, value=test_result)

    # 测试登录接口
    @data(*login_cases)
    def test_login(self, login_case):
        my_log.info('登录接口：开始执行第{}条用例：{}!!!'.format(login_case.id,login_case.title))
        r = session.request(method=method, url=login_url, headers=headers, data=login_case.data)
        my_log.info(r.text)
        result = r.json()['status']
        try:
            self.assertEqual(login_case.expected, result)
            test_result = 'PASS'
        except AssertionError as e:
            test_result = 'FAILD'
            msg = '测试失败，失败原因：{}'.format(e)
            text = r.text
            my_log.error(msg)
            my_log.error(text)
            raise e
        finally:
            login.write_data(row=login_case.id + 1, column= 6, value=result)
            login.write_data(row=login_case.id + 1, column= 7, value=test_result)

    # 测试充值接口
    @data(*recharge_cases)
    def test_recharge(self, recharge_case):
        my_log.info('充值接口：开始执行第{}条用例：{}!!!'.format(recharge_case.id, recharge_case.title))
        r = session.request(method=method, url=recharge_url, headers=headers, data=recharge_case.data)
        my_log.info(r.text)
        result = int(r.json()['code'])
        try:
            self.assertEqual(recharge_case.expected, result)
            test_result = 'PASS'
        except AssertionError as e:
            test_result = 'FAILD'
            msg = '测试失败，失败原因：{}'.format(e)
            text = r.text
            my_log.error(msg)
            my_log.error(text)
            raise e
        finally:
            recharge.write_data(row=recharge_case.id + 1, column=6, value=result)
            recharge.write_data(row=recharge_case.id + 1, column=7, value=test_result)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
