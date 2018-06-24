# @Time     :   2018-6-24 23:03
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   User.py
# @Software :   PyCharm


class User:

    def __str__(self):
        return "用户名为%s,密码为%s" % (self.username, self.password)

    def setPassword(self, password):
        if len(password) >= 6:
            self.password = password
        else:
            print("密码%s过短" % password)


user1 = User()
user1.username = "andbf"
# user1.password = "1234"
user1.setPassword("1234")
user1.setPassword("123456")
print(user1)
