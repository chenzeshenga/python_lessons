# @Time     :   2018-5-28 21:23
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   localvarible.py
# @Software :   PyCharm

b = "global"


def test1():
    a = 200
    print(a)
    global b
    b = "local"
    print(b)


# print(a)
test1()
