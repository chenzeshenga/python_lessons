# @Time     :   2018-6-4 23:39
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   recursion_dir_files.py
# @Software :   PyCharm

import os


def recursion_dir(dir):
    if os.path.isdir(dir):
        for f in os.listdir(dir):
            recursion_dir(f)
    else:
        print(os.path.abspath(dir))
        if read_file(dir):
            print(os.path.abspath(dir))


def read_file(file):
    flag = False
    f = open(file)
    while True:
        line = f.readline()
        if line == "":
            break
        elif "chenzeshenga" in line:
            print(line)
            flag = True
            break
    f.close()
    return flag


path = os.path.join("F:\\", "Idea_PyCharm")
path = os.path.join(path, "com", "chenzeshenga", "study", "Condition.py")
recursion_dir(path)
