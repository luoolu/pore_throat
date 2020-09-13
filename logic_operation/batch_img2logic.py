# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 下午4:10
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : img2logic.py
# @Software: PyCharm
import glob
import os

import cv2
import numpy as np


if __name__ == '__main__':
    base_name = ''
    counter = 0
    for filename1 in sorted(glob.glob('/home/luolu/Downloads/data/yashi_bp/pore_throat_img/pore_extract_10Xcrop/*.png')):
        for filename2 in sorted(glob.glob('/home/luolu/Downloads/data/yashi_bp/pore_throat_img/pore_cleaned/*.png')):
            img1 = cv2.imread(filename1)
            img2 = cv2.imread(filename2)
            base_name1 = os.path.basename(filename1)
            base_name2 = os.path.basename(filename2)
            if base_name2.__eq__(base_name1):
                # height, width, channels = img.shape
                print(base_name2)


                # subtract = cv2.subtract(img1, img2)
                add = cv2.add(img1, img2)
                # bitwise_xor = cv2.bitwise_not(img1, img2)
                # bitwise_and = cv2.bitwise_and(img1, img2)


                cv2.imwrite("/home/luolu/Downloads/data/yashi_bp/pore_throat_img/img2add/" + base_name1, add)

                # cv2.waitKey(0)
                # cv2.destroyAllWindows()