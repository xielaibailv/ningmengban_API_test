from kongkong_0116_从Excel读写用例.test_case.test_case import TestCases
from kongkong_0116_从Excel读写用例.test_case import test_case
from kongkong_0116_从Excel读写用例 import test_case
import HTMLTestRunnerNew
import unittest
from kongkong_0116_从Excel读写用例.conf_file.read_conf import ReadConf


# 从配置文件获取执行接口
conf_file = '../conf_file/conf.ini'
api = ReadConf(conf_file).get_value('RUN', 'api')

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(TestCases))

# 使用了ddt，不能再像这样执行单个用例
# if api == 'register':
#     suite.addTest(loader.loadTestsFromName('test_case.TestCases.test_register'))
# elif api == 'login':
#     suite.addTest(loader.loadTestsFromName('test_case.TestCases.test_login'))
# elif api == 'recharge':
#     suite.addTest(loader.loadTestsFromName('test_case.TestCases.test_recharge'))
# elif api == 'all':
#     suite.addTest(loader.loadTestsFromTestCase(TestCases))

report_path = '../test_result/test_report.html'
with open(report_path, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='前程贷注册登录充值接口测试报告',
                                              tester='空空')
    runner.run(suite)
