from test_qianchengdai.test_case.test_case import TestLogin
import HTMLTestRunnerNew
import unittest

# suite:集合套件,专门存储加载测试用例
suite = unittest.TestSuite()
# 实例化TestLoader，从测试类里获取用例
loader = unittest.TestLoader()
# 把获取到的用例添加到测试集合套件
suite.addTest(loader.loadTestsFromTestCase(TestLogin))

with open('../test_result/test_report.html','wb') as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(f, verbosity=2, title='qianchengdai_test_report', tester='YOYO')
    runner.run(suite)
