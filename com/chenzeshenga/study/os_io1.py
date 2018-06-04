# @Time     :   2018-6-4 23:09
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   os_io1.py
# @Software :   PyCharm
import os

# os.rename("copy-test1.txt", "copy-test2.txt")

files_list = os.listdir(".")
print(files_list)

for file in files_list:
    print(os.path.abspath(file))
