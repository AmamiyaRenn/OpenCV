'''
Description: 图像加噪与降噪
Version: 第一版
Author: 雨宫
Date: 2021-08-25 21:20:28
LastEditors: 雨宫
LastEditTime: 2021-08-26 21:45:47
'''
import cv2 as cv
import numpy as np


#*防止图像信息溢出
def clamp(pv):
    if pv > 255:
        return 255
    elif pv < 0:
        return 0
    else:
        return pv


#*增加高斯噪声
def gaussian_noise(image):
    height, width, channels = image.shape
    for row in range(0, height):
        for col in range(0, width):
            s = np.random.normal(0, 15, 3)
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])


#*增加椒盐噪声
def sp_noise(image, prob):  #prob为占比，一般设为0.05
    height, width, channels = image.shape
    sum_points = height * width
    noise_points = int(sum_points * prob)
    for i in range(noise_points):
        row = np.random.randint(0, height - 1)
        col = np.random.randint(0, width - 1)
        if np.random.random() < 0.5:
            image[row, col] = 0
        else:
            image[row, col] = 255


#*读图
img = cv.imread('d:\Code\python3\OpenCV\day2task1\SuperSmashBros.jpg')
#*图像加噪与降噪
sp_noise(img, 0.05)
#gaussian_noise(img)
#img = cv.GaussianBlur(img, (5, 5), 0)  #高斯矩阵长宽都为5，标准差为0
#img = cv.blur(img, (3, 3))  #均值模糊
img = cv.medianBlur(img, 3)  #中值模糊
#*画图
cv.imwrite('day2task1/mBlur_spNoise.jpg', img)
cv.imshow('demo', img)
cv.waitKey(0)
cv.destroyAllWindows()
