import unittest
from ddt import ddt,data
import requests


@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data
    def test_login(self):
        r = requests.post(url=url, headers=headers, data=data)
        result = r.json()['status']
        try:
            self.assertTrue(expected, result)
            test_result = 'PASS'
        except Exception as e:
            test_result = 'FAILD'
            msg = '测试失败，失败原因：{}'.format(e)
            raise e
        finally:
            pass