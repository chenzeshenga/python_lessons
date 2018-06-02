# @Time     :   2018-6-2 21:31
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   param.py
# @Software :   PyCharm


def test1(x, y):
    x.replace("c", "C")
    y.append(10)
    print(id(x))
    print(id(y))


a = "adbhskjfcc"
b = [1, 2, 2, 3]
print(id(a))
print(id(b))

test1(a, b)
