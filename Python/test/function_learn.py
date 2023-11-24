#!/usr/bin/python3

# 计算面积函数
def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

'''
print_welcome("Python")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))
'''

print(__name__, 'run2-outside')    # 它会print出【__main__ run1-outside】
if __name__ =='__main__':
    print(__name__, 'run2-inside') # 它会print出【__main__ run1-inside】