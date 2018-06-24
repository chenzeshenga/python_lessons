# @Time     :   2018-6-25 0:03
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   A.py
# @Software :   PyCharm

# 多继承
# 多继承的顺序跟定义有关系，谁写在前面，这个类就是直接继承
class A:
    def test(self):
        print("A test")


class B:
    def test(self):
        print("B test")


class C(A, B):
    def test1(self):
        print("C test1")

    # def test(self):
    #     print("C test")


c = C()
print(C.__mro__)
