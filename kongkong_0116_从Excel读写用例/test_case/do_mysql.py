import contextlib
from kongkong_0116_从Excel读写用例.test_data.do_excel import DoExcel
from kongkong_0116_从Excel读写用例.test_case.mysql import MySQL


# class DoMySQL:
#     """从数据库查询需要的数据然后写入Excel"""

with contextlib.closing(MySQL()) as mysql:
    sql = "select max(MobilePhone) from member"
    data = int(mysql.select(sql)[0])
print(type(data),data)

wb = DoExcel('../test_data/test_data.xlsx','register')
wb.write_data(row=2, column=3, value=data + 1)
wb.write_data(row=3, column=3, value=data + 2)
wb.write_data(row=4, column=3, value=data + 3)
wb.write_data(row=5, column=3, value=data + 4)
wb.write_data(row=6, column=3, value=data + 5)

