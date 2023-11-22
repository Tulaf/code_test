#!/usr/bin/python3

import os
if os.path.exists("./newdir"):
    print("file exist!")
else:
    os.mkdir('newdir')

with open("./newdir/新建文件.txt", "w") as file:
    file.write("欢迎使用Python!")

os.rename("./newdir/新建文件.txt", "./newdir/test.txt")

str = os.getcwd()
print("current path ：",str)


os.remove("./newdir/test.txt")
os.rmdir("./newdir")
