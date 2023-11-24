#!/usr/bin/python3

print("hello python world!")

x="a"
y="b"
# 换行输出
print(x)
print(y)

print ('---------')
# 不换行输出
print(x,end=" ")
print(y)

print(x,end="@")
print(y)

#变量

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print(counter)
print(miles)
print(name)

a = b = c = 1
d,e,f = 1,2,"john"
print(a,b,c,d,e,f)

#字符串
str = 'Hello Python World!'

print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str[1:-1:2])
print(str*2)
print(str+"TEST")

#列表

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print(list)               # 输出完整列表
print(list[0])            # 输出列表的第一个元素
print(list[1:3])          # 输出第二个至第三个元素 
print(list[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)       # 输出列表两次
print(list + tinylist)    # 打印组合的列表

#元组
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
 
print(tuple)               # 输出完整元组
print(tuple[0])            # 输出元组的第一个元素
print(tuple[1:3])          # 输出第二个至第四个（不包含）的元素 
print(tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)       # 输出元组两次
print(tuple + tinytuple)   # 打印组合的元组


#字典
dict = {}
dict['one'] = "This is one"
dict[2] = "this is two"

tinydict = {
        'name': 'rubot',
        'code': 'python',
        'role': 'computer'
}

print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

#数学运算符
a = 21
b = 10
c = 0
 
c = a + b
print("1 - c 的值为：", c)
 
c = a - b
print("2 - c 的值为：", c)
 
c = a * b
print("3 - c 的值为：", c)
 
c = a / b
print("4 - c 的值为：", c)
 
c = a % b
print("5 - c 的值为：", c)
 
# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b 
print("6 - c 的值为：", c)
 
a = 10
b = 5
c = a//b 
print("7 - c 的值为：", c)


#逻辑运算符

#赋值运算符

#位运算符

#成员运算符
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")

if ( b not in list ):
   print("2 - 变量 b 不在给定的列表中 list 中")
else:
   print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if ( a in list ):
   print("3 - 变量 a 在给定的列表中 list 中")
else:
   print("3 - 变量 a 不在给定的列表中 list 中")
   
a = 20
b = 20
 
if ( a is b ):
   print("1 - a 和 b 有相同的标识")
else:
   print("1 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print("2 - a 和 b 没有相同的标识")
else:
   print("2 - a 和 b 有相同的标识")
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print("3 - a 和 b 有相同的标识")
else:
   print("3 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print("4 - a 和 b 没有相同的标识")
else:
   print("4 - a 和 b 有相同的标识")

# for循环

for letter in 'Python':     # 第一个实例
   print("当前字母: %s" % letter)
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print ('当前水果: %s'% fruit)
for index in range(len(fruits)):
   print ('当前水果 : %s' % fruits[index])
print ("Good bye!")

#嵌套逻辑
#打印小于100的素数
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print(i, " 是素数")
   i = i + 1

print("Good bye!")


