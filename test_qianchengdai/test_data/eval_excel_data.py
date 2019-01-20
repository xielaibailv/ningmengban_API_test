from test_qianchengdai.test_data.do_excel import DoExcel


# 从Excel获取测试数据
register = DoExcel('../test_data/test_data.xlsx', 'register')
login = DoExcel('../test_data/test_data.xlsx', 'login')
recharge = DoExcel('../test_data/test_data.xlsx', 'recharge')
register_data = register.read_data()   # 注册数据
login_data = login.read_data()         # 登录数据
recharge_data = recharge.read_data()   # 充值数据


class EvalExcelData:
    """将Excel里的测试数据转化成请求可以使用的字典格式"""

    # 转化注册用例
    @staticmethod
    def register_cases():
        register_cases = []
        for each in register_data:
            register_case = {}
            register_case['mobilephone'] = each.phone
            register_case['regname'] = each.name
            register_case['pwd'] = each.pwd
            register_cases.append(register_case)
        return register_cases

    # 转化登录用例
    @staticmethod
    def login_cases():
        login_cases = []
        for each in login_data:
            login_case = {}
            login_case['mobilephone'] = each.phone
            login_case['pwd'] = each.pwd
            login_cases.append(login_case)
        return login_cases

    # 转化充值用例
    @staticmethod
    def recharge_cases():
        recharge_cases = []
        for each in recharge_data:
            recharge_case = {}
            recharge_case['mobilephone'] = each.phone
            recharge_case['amount'] = each.amount
            recharge_cases.append(recharge_case)
        return recharge_cases



if __name__ == '__main__':
    print(EvalExcelData().register_cases())

