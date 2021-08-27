'''
Description: 简单的图像处理
Version: 第一版
Author: 雨宫
Date: 2021-08-25 16:33:42
LastEditors: 雨宫
LastEditTime: 2021-08-26 22:26:03
'''
import cv2 as cv

print("Hello OpenCV!")
#img = cv.imread("D:\Code\python3\OpenCV\picture\sea.png")
#//img = cv2.imread("d:\\Sharp\\Study\\机器人队\\参考资料\\控制\\Vision\\Day1\\4. 图像要素\\sea.png")
img = cv.imread("D:\Code\python3\OpenCV\day1picture\sea.png",
                cv.IMREAD_GRAYSCALE)
#img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
img = img[0:480, 0:640]  #*图像裁剪
height, width = img.shape  #*获得图像高、宽

fp = open('picture\grayResult.txt', 'a')  #*打开图像
for i in range(height):  #*对灰度大于150的像素点进行记录
    for j in range(width):
        if img.item(i, j) > 150:
            point = [i, j]
            points_w = str(point)
            fp.writelines(points_w)
            fp.write('\n')
fp.write('\n')
fp.close()  #*关闭图像

cv.imwrite("day1picture\sea_cut_gray.png", img)
cv.imshow("demo", img)
cv.waitKey(0)
cv.destroyAllWindows()