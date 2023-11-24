#!/usr/bin/python3

str = input("请输入: ")
print("你输入的内容是：",str)

#file operation
fo = open('testfile.txt',mode='w+',encoding='utf8')
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)


fo.write( "www.nuclei.com!\nVery good site!\n")

position = fo.seek(0, 0)

str = fo.read(10)

print("读取的字符串是 : ", str)
position = fo.tell()
print("当前文件位置 : ", position)

str = fo.read(4)
print ("重新读取字符串:", str)
fo.close()

