# @Time     :   2018-6-2 22:14
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   recursion.py
# @Software :   PyCharm

def recursion(n):
    if n == 1 or n == 2:
        return 1
    return recursion(n - 1) + recursion(n - 2)


nums = []

for i in range(1, 20):
    nums.append(recursion(i))

print(nums)
