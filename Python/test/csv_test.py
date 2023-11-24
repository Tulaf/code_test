#!/usr/bin/python3

import csv
from function_learn import area


dict = {}
list = []

# 打印csv的每一行

with open('test.csv') as f:
    csv_reader = csv.reader(f,dialect='excel')
    for row in csv_reader:
        print(row)
        #将test.csv内容读入列表l，每行为其一个元素，元素也为list
        list.append(row)
'''
with open('1.csv','wt') as f2:
    cw = csv.writer(f2)
    for item in list:
        #采用writerow()方法,将列表的每个元素写到csv文件的一行
        cw.writerow(item)

with open("test.csv") as f3:
    dict = csv.DictReader(f3, fieldnames=None, restkey=None, restval=None, dialect='excel')
    print(dict.__next__())

area = area(4,5)
print("area :",area)
'''

print(__name__, 'run1-outside')    # 它会print出【__main__ run1-outside】
if __name__ =='__main__':
    print(__name__, 'run1-inside') # 它会print出【__main__ run1-inside】