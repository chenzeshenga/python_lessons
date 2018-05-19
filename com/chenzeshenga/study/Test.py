# @Time     :   2018-5-19 14:39
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   Test.py
# @Software :   PyCharm

names = ["12", "23", "34", "56"]
names2 = ("12", "23", "34", "56")
j = 0
print("order\tvalue")
for i in names:
    j += 1
    print("%d\t%s" % (j, i))
print()
for i in names2:
    j += 1
    print("%d\t%s" % (j, i))
print("---------------")
# 枚举
for i, item in enumerate(names, 1):
    print("%d\t%s" % (i, item))
