'''
Description: 轮廓绘制
Version: 第一版
Author: 雨宫
Date: 2021-08-26 08:40:22
LastEditors: 雨宫
LastEditTime: 2021-08-26 21:58:43
'''
import cv2 as cv
import numpy as np
#*颜色阈值目录
ball_color = 'black'
color_dist = {
    'black': {
        'lower': np.array([230, 230, 230]),
        'upper': np.array([255, 255, 255])
    }
}

img = cv.imread('d:\Code\python3\OpenCV\day2task2\Akashi.jpg')
img_copy = cv.GaussianBlur(img, (5, 5), 0)  #*高斯模糊降噪
#hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)#*BGR转hsv域
#hsv = cv.erode(hsv, None, iterations=2)#*腐蚀hsv图像
img_copy = cv.erode(img_copy, None, iterations=1)  #*腐蚀图像
img_copy = cv.inRange(  #*二值化获得感兴趣图像
    img_copy, color_dist[ball_color]['lower'], color_dist[ball_color]['upper'])
contours, hierarchy = cv.findContours(  #*寻找轮廓，参数为外部单层轮廓，保存所有轮廓点
    img_copy, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(img, contours, -1, (0, 255, 0), 2,
                lineType=cv.LINE_AA)  #*画轮廓，参数为-1（所有轮廓），色彩，线宽，线形为反锯齿

cv.imwrite('day2task2/The face contours of Akashi.jpg', img)
cv.imshow('demo', img)
cv.waitKey(0)
cv.destroyAllWindows()