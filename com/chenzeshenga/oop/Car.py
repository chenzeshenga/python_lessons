# @Time     :   2018-6-12 22:03
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   Car.py
# @Software :   PyCharm


class Car:
    def start(self):
        print("start car")

    def print_car_info(self):
        print("%s,%s" % (self.name, self.color))


c1 = Car()
c2 = Car()

c1.name = "abc"
c1.color = "red"

c1.print_car_info()
c1.start()
c2.start()
