# 10.9 Data Compression
# Program.py

from testApiController.user.userController import UserController

userCtrl = UserController()
# res = userCtrl.list()
# print(f'http code={res.code}')
# for u in res.data:
#     print(u.toString())

res = userCtrl.get()
print(f'http code={res.code}')
print(res.data.toString())