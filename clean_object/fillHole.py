# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 下午2:22
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : fillHole.py
# @Software: PyCharm

import cv2
import numpy as np

'''
图像说明：
图像为二值化图像，255白色为目标物，0黑色为背景
要填充白色目标物中的黑色空洞
'''


def FillHole(imgPath, SavePath):
    im_in = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("/home/luolu/Downloads/data/yashi_bp/pore_throat_img/im_in_fill_hole_16-0460_5.png", im_in)
    # 复制 im_in 图像
    im_floodfill = im_in.copy()

    # Mask 用于 floodFill，官方要求长宽+2
    h, w = im_in.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # floodFill函数中的seedPoint对应像素必须是背景
    isbreak = False
    for i in range(im_floodfill.shape[0]):
        for j in range(im_floodfill.shape[1]):
            if (im_floodfill[i][j] == 0):
                seedPoint = (i, j)
                isbreak = True
                break
        if (isbreak):
            break

    # 得到im_floodfill 255填充非孔洞值
    cv2.floodFill(im_floodfill, mask, seedPoint, 0)

    # 得到im_floodfill的逆im_floodfill_inv
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)

    # 把im_in、im_floodfill_inv这两幅图像结合起来得到前景
    im_out = im_in | im_floodfill_inv

    # 保存结果
    cv2.imwrite(SavePath, im_out)

imgPath = "/home/luolu/Downloads/data/yashi_bp/pore_throat_img/pore_extract_10Xcrop/16-0460_5.png"
SavePath = "/home/luolu/Downloads/data/yashi_bp/pore_throat_img/fill_hole_16-0460_5.png"
FillHole(imgPath, SavePath)