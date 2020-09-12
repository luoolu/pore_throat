# -*- coding: utf-8 -*-
# @Time    : 2020/9/12 下午3:28
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : mv_noise.py
# @Software: PyCharm
import cv2
import numpy as np

img = cv2.imread('/home/luolu/Downloads/data/yashi_bp/pore_throat_img/pore_extract_10Xcrop/16-0460_5.png')

img_bw = 255 * (cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) > 5).astype('uint8')

se1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
se2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (32, 32))
mask = cv2.morphologyEx(img_bw, cv2.MORPH_CLOSE, se1)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)

mask = np.dstack([mask, mask, mask]) / 255
out = img * mask

cv2.imwrite("/home/luolu/Downloads/data/yashi_bp/pore_throat_img/cleaned_16-0460_5.png", out)

# cv2.imshow('', masked_img)
# cv2.waitKey()
