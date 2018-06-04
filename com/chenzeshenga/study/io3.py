# @Time     :   2018-6-4 23:02
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   io3.py
# @Software :   PyCharm

file1 = open("test1.txt")

file1.seek(0, 0)
position1 = file1.tell()
file1.seek(0, 2)

file1.close()
