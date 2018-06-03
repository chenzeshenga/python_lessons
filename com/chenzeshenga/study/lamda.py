# @Time     :   2018-6-3 15:10
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   lamda.py
# @Software :   PyCharm

method1 = lambda x, y: x + y

print(method1(2, 3))


def fun(a, b, func):
    result = func(2, b)
    return result


print(fun(2, 3, lambda x, y: x + y))

stus = [{"name": "123"}, {"name": "8"}, {"name": "3"}, {"name": "4"}]
stus.sort(key=lambda x: x["name"])

print(stus)
