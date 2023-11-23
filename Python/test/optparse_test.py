#!/usr/bin/python3

from optparse import OptionParser  #import OptionParser类

optParser = OptionParser() #创建一个OptionParser对象

optParser.add_option('-f','--file',action='store',type='string',dest='filename',default='hello.txt')
optParser.add_option("-v", "--vision", action='store_true', dest="verbose", default=False, help="make lots of noise[default]")

#optParser.parse_args() 解析并返回一个字典和列表
#字典中的key是我们所有的add_option()函数中的dest的参数值，value是add_option()函数中的default的参数或者是用户传入optParser.parse_args()的参数
#一个由positional arguments组成的列表

# fakeArgs=['--file','tset.txt','-v','how are you']

option, args=optParser.parse_args()

if option.verbose == True:
    print("verbose true")

# op, ar = optParser.parse_args(fakeArgs)
# print("option: ",option)
# print("args:", args)
# print("op:", op)
# print("ar:", ar)

