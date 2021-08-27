'''
Description: Harris，sift，orb算法提取特征量
Version: 第一版
Author: 雨宫
Date: 2021-08-26 15:26:14
LastEditors: 雨宫
LastEditTime: 2021-08-26 22:18:23
'''
import cv2
import numpy as np

img = cv2.imread('d:\Code\python3\OpenCV\day2task4\Megumi is Sleeping.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #*转灰度域方便后续算法操作
#*Harris算法找角点
#gray = np.float32(gray)  #*灰度值浮点化，目前没有测试取消该条代码的效果
#harris = cv2.cornerHarris(gray, 2, 3, 0.04)  #*Harris算法找角点
#dst = cv2.dilate(harris, None)  #*膨胀角点信息
#threshold = 0.01 * dst.max()  #*对膨胀后的角点信息取其中的max值（目前不清楚max函数作用）乘上0.01的信息作为阈值
#img[dst > threshold] = [0, 0, 255]  #*对大于阈值部分的角点信息进行色彩覆盖

#*SIFT算法提取特征点
sift = cv2.SIFT_create()  #*初始化sift
keypoints = sift.detect(gray, None)  #*对灰度域图像进行特征点检测
cv2.drawKeypoints(
    img,  #*绘制特征点
    keypoints,
    img,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  #*绘制时同时绘制方向，尺度和位置

#*ORB算法提取特征点
#orb = cv2.ORB_create()  #*初始化orb
#keypoints = orb.detect(img, None)  #*对灰度域图像进行特征点检测
#cv2.drawKeypoints(img, keypoints, img, color=(0, 0, 255), flags=0)

cv2.imwrite('day2task4/Megumi_sift.jpg', img)
cv2.imshow('demo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()