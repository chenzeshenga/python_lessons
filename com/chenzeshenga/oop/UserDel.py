# @Time     :   2018-6-24 23:03
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   User.py
# @Software :   PyCharm


class User:
    def __init__(self):
        print("method init")

    def __del__(self):
        print("对象销毁")


user1 = User()
user2 = user1
del user1
print("111111111111111")
# del user2
print("222222222222222222")
