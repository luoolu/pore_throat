# -*- coding: utf-8 -*-
# @Time    : 2020/9/12 下午3:28
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : mv_noise.py
# @Software: PyCharm
import glob
import os

import cv2
import numpy as np

if __name__ == '__main__':
    base_name = ''
    counter = 0
    for filename in sorted(glob.glob('/home/luolu/Downloads/data/yashi_bp/pore_throat_img/pore_extract_10Xcrop/*.png')):
        img = cv2.imread(filename)
        # height, width, channels = img.shape
        print(filename)
        base_name = os.path.basename(filename)

        img_bw = 255 * (cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) > 5).astype('uint8')

        se1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        se2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (32, 32))
        mask = cv2.morphologyEx(img_bw, cv2.MORPH_CLOSE, se1)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)

        mask = np.dstack([mask, mask, mask]) / 255
        out = img * mask

        cv2.imwrite("/home/luolu/Downloads/data/yashi_bp/pore_throat_img/cleaned_10xcrop_src/" + base_name, out)

        # cv2.imshow('', masked_img)
        # cv2.waitKey()
