# -*- coding: utf-8 -*-
# @Time : 2020/4/2 上午11:12
# @Author : LuoLu
# @FileName: median_filter.py
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
    for filename in sorted(glob.glob('/home/luolu/Downloads/data/yashi_bp/pore_throat_img/pore_cleaned/*.png')):
        img = cv2.imread(filename, 0)
        # height, width, channels = img.shape
        print(filename)
        base_name = os.path.basename(filename)

        median = cv2.medianBlur(img, 31)
        

        cv2.imwrite("/home/luolu/Downloads/data/yashi_bp/pore_throat_img/pore_filtered/" + base_name, median)

        # cv2.namedWindow('img', flags=2)
        # cv2.imshow('img', compare)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()