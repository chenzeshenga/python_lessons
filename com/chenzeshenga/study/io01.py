# @Time     :   2018-6-4 22:25
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   io01.py
# @Software :   PyCharm

file1 = open("test1.txt", "w")
file1.write("hello io stream\n")
file1.write("hello io stream\n")
file1.write("hello io stream\n")
file1.close()

file1 = open("test1.txt", "r")
# print(file1.read())
# print(file1.readlines())
print(file1.readline())
print(file1.readline())
file1.close()
