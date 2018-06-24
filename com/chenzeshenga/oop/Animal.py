# @Time     :   2018-6-24 23:44
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   Animal.py
# @Software :   PyCharm


class Animal:

    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")


# 继承
class Dog(Animal):
    def bark(self):
        print("bark")


class Cat(Animal):
    def catch_mice(self):
        print("catch mice")


dog = Dog()
dog.eat()
dog.sleep()
dog.bark()

cat = Cat()
cat.eat()
cat.sleep()
cat.catch_mice()
