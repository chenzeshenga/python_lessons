# @Time     :   2018-6-24 23:03
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   User.py
# @Software :   PyCharm

# 如果属性或者方法前面加上两个下划线"__"，
# 则这个方法或者属性为私有的


class User:
    # 隐藏属性
    def __init__(self, password):
        if len(password) >= 6:
            self.__password = password
        else:
            print("密码%s过短" % password)

    def __str__(self):
        return "密码为%s" % self.__password

    def get_password(self, ):
        return self.__password


user1 = User("123456")
print(user1)
# print(user1.__password)
print(user1.getPassword())
