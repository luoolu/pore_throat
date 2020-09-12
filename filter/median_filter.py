# -*- coding: utf-8 -*-
# @Time : 2020/4/2 上午11:12
# @Author : LuoLu
# @FileName: median_filter.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com

import cv2
import numpy as np

img = cv2.imread('/data/yashi_qscan/mask/fen_mask.png')
median = cv2.medianBlur(img, 3)
compare = np.concatenate((img, median), axis=1) #side by side comparison

cv2.namedWindow('img', flags=2)
cv2.imshow('img', compare)
cv2.waitKey(0)
cv2.destroyAllWindows()