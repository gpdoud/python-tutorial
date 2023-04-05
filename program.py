# 10.9 Data Compression
# Program.py

from testApiController.user.userController import UserController

userCtrl = UserController()
# res = userCtrl.list()
# print(f'http code={res.code}')
# for u in res.data:
#     print(u.toString())

from testApiController.user.user import User
user = User()
user.id = 7
user.username = 'zzx'
user.password = 'zzx'
user.firstname = 'zzx'
user.lastname = 'zzx'
user.phone = 'zzx'
user.email = 'zzx'
user.isReviewer = False
user.isAdmin = False
jsonuser = user.toJson()
res = userCtrl.delete(user.id)
print(f'code={res.code}')