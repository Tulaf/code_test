import cv2          #opencv 读取的格式是RGB
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import hexdump

#图像显示
def cv_show(name,img):
    cv2.imshow(name,img)    #图像显示
    cv2.waitKey(0)       #0:无限时间等待 1000:1s
    cv2.destroyAllWindows() #任意键关闭所有Windows


# 文件 转 数组
def file_to_numpy(path_file):
    image_np = cv2.imread(path_file)
    return image_np

## 图片读取（cv2.IMREAD_GRAYSCALE：灰度图像 cv2.IMREAD_COLOR：彩色图像）
img=cv2.imread('dooooooooooooooooooooog.jpg',cv2.IMREAD_COLOR)




# cv_show("mydog",img)
#图片像素矩阵(...x...x...)
img.shape
# print (img.shape)
# print(file_to_numpy('dooooooooooooooooooooog.jpg'),file=log)

with open("dooooooooooooooooooooog.jpg", "rb") as f:
    image_bytes_data = f.read()

with open("pic.log", "a", encoding='utf-8') as log:
    print(hexdump.hexdump(image_bytes_data), file=log)

# 打开图片文件
# image = Image.open('dooooooooooooooooooooog.jpg')

# # 将图片转换为像素数据
# pixels = list(image.getdata())

# # 打印像素数据
# print(pixels)


# # 假设你有一个形状为(height, width, 3)的NumPy数组
# array = np.random.rand(100, 100, 3) * 255
# # 将数组转化为图片
# image = Image.fromarray(array.astype(np.uint8))
# # 显示图片
# image.show()

#颜色通道提取
# b,g,r=cv2.split(img) #色彩提取之前不可以灰度处理

# r_data = r.flatten().tolist()
# g_data = g.flatten().tolist()
# b_data = b.flatten().tolist()

# print(r_data,file=log)
# print(g_data,file=log)
# print(b_data,file=log)



log.close()
'''
#图片保存
cv2.imwrite('mycat.png',img)


#图片截取
half_dog=img[0:500,0:200] 
cv_show('maydog.jpeg',half_dog)





#颜色通道合并
img2=cv2.merge((b,g,r))
cv_show('color_merge',img2)


# 对图片进行边界填充
top_size,bottom_size,left_size,right_size = (50,50,50,50)

replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv2.BORDER_CONSTANT, value=0)
plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()

# 图像融合：
img_cat=cv2.imread('macat.png')
img_dog=cv2.imread('dooooooooooooooooooooog.jpg')
img_dog = cv2.resize(img_dog, (1000, 2000))           #将两个图片改为同样大小
res = cv2.addWeighted(img_cat, 0.4, img_dog, 0.6, 0)#猫占0.4权重，狗占0.6权重
plt.imshow(res)

# 更改图片长宽比
res = cv2.resize(img, (0, 0), fx=3, fy=1)
cv_show("resize",res)



hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv_show("rgb_hsv",hsv)

img_gray=cv2.imread("dooooooooooooooooooooog.jpg",cv2.IMREAD_GRAYSCALE)
ret, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

#################
img = cv2.imread('mycat.png')
blur = cv2.blur(img, (3, 3))# 均值滤波
box1 = cv2.boxFilter(img,-1,(3,3), normalize=True)  # 方框滤波
box2 = cv2.boxFilter(img,-1,(3,3), normalize=False) # 方框滤波
aussian = cv2.GaussianBlur(img, (5, 5), 1)  # 高斯滤波
median = cv2.medianBlur(img, 5)  # 中值滤波
res = np.hstack((blur,aussian,median))
'''


'''
#视频读取
vc = cv2.VideoCapture('ikun.mp4')
# 检查是否打开正确
if vc.isOpened():
    oepn, frame = vc.read()
else:
    open = False

#展示视频
while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)
        cv2.imshow('ikun', gray)
        if cv2.waitKey(100) & 0xFF == ord('q'):     #播放完成或者按下“q”退出
            break
vc.release()
cv2.destroyAllWindows()
'''
