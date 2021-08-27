'''
Description: 霍夫变换拟合直线
Version: 第一版
Author: 雨宫
Date: 2021-08-26 11:15:59
LastEditors: 雨宫
LastEditTime: 2021-08-27 10:09:43
'''
import cv2 as cv
import numpy as np

img = cv.imread('day2task3\Megumi.jpg')

img = cv.GaussianBlur(img, (3, 3), 0)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #*转灰度域以便霍夫变换
edges = cv.Canny(gray, 25, 50, apertureSize=3)  #*Canny算法获得边缘信息
#*概率霍夫变换算法
lines = cv.HoughLinesP(
    edges,  #*边缘
    0.5,  #*单位rho
    np.pi / 480,  #*单位theta
    30,  #*票数阈值
    minLineLength=70,  #*最小线长
    maxLineGap=10)  #*最大线间距允许值
for line in lines:  #*画线
    cv.line(img, (line[0][0], line[0][1]), (line[0][2], line[0][3]),
            (0, 255, 0), 2)

#cv.imwrite('day2task3/Megumi_Lines.jpg', img)
cv.imshow('demo', img)
cv.waitKey(0)
cv.destroyAllWindows()