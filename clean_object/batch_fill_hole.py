# -*- coding: utf-8 -*-
# @Time : 2020/4/13 下午3:59
# @Author : LuoLu
# @FileName: fill_hole.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com
import glob
import os

import cv2
import numpy as np


if __name__ == '__main__':
    base_name = ''
    counter = 0
    for filename in sorted(glob.glob('/home/luolu/Downloads/data/yashi_bp/pore_throat_img/pore_mask/*.png')):
        img = cv2.imread(filename, 0)
        # height, width, channels = img.shape
        print(filename)
        base_name = os.path.basename(filename)

        # img = cv2.subtract(255, img)
        # cv2.imshow('bw_change', img)

        img[img != 255] = 0

        # flood fill background to find inner holes
        holes = img.copy()
        cv2.floodFill(holes, None, (0, 0), 255)

        # invert holes mask, bitwise or with img fill in holes
        holes = cv2.bitwise_not(holes)
        filled_holes = cv2.bitwise_or(img, holes)
        cv2.imwrite("/home/luolu/Downloads/data/yashi_bp/pore_throat_img/filled_holes/" + base_name, filled_holes)
        # cv2.imshow('filled_holes', filled_holes)
        # cv2.waitKey()
