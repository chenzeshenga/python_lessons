# @Time     :   2018-6-27 22:53
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   override.py
# @Software :   PyCharm

class Animal:

    def __init__(self):
        print("Animal")

    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")


# 继承
class Dog(Animal):

    # init 方法和父类的方法名字一样就被称为重写了父类的方法，
    # 如果子类中对父类的方法重写了，就会优先调用子类的方法
    def __init__(self):
        # 主动调用父类的init方法
        super().__init__()
        print("Dog")

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
