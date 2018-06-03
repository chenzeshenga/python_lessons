# @Time     :   2018-6-2 21:41
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   student.py
# @Software :   PyCharm


def print_menu():
    print("学生管理系统".center(20))
    print("输入1： 添加学生")
    print("输入2： 查询学生")
    print("...")


def add_student():
    name = input("name:")
    age = input("age:")
    qq = input("qq:")
    stu = {}
    stu["name"] = name
    stu["age"] = age
    stu["qq"] = qq
    stus.append(stu)
    print("success")


def del_student(name):
    student = query_student(name)
    stus.remove(student)


def query_student(name):
    for stu in stus:
        if stu["name"] == name.strip():
            print(stu)
            return stu
    else:
        print("can't fine name %s" % name)


stus = []

print_menu()
while True:
    operate = input("请输入操作： ")
    if operate == "1":
        add_student()
    elif operate == "2":
        name = input("name=")
        query_student(name)
    elif operate == "3":
        name = input("name=")
        del_student(name)
    else:
        break
