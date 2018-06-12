# @Time     :   2018-6-12 22:47
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   Person.py
# @Software :   PyCharm


class Person:
    # def __init__(self):
    #     print("init")
    # def __new__():
    #     print("123")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("init with parameters,%s,%s" % (name, age))

    def work(self):
        print("work")


# p1 = Person()
p2 = Person("abd", 99)
