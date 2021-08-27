'''
Description: Open3d可视化点云
Version: 第一版
Author: 雨宫
Date: 2021-08-26 20:50:24
LastEditors: 雨宫
LastEditTime: 2021-08-26 22:18:40
'''
import open3d as o3d

pcd = o3d.io.read_point_cloud('day2task5/bunny.pcd')  #*点云读入
o3d.visualization.draw_geometries([pcd], width=800, height=800)  #*可视化点云
