# @Time     :   2018-6-4 22:47
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   io02.py
# @Software :   PyCharm

source_file = "test1.txt"
dest_file = "copy-" + source_file
source_f = open(source_file)
dest_f = open(dest_file, "w")
content=source_f.read()
dest_f.write(content)

source_f.close()
dest_f.close()