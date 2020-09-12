# -*- coding: utf-8 -*-
# @Time : 2020/4/2 上午11:28
# @Author : LuoLu
# @FileName: conservative_smoothing.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com
import cv2
import numpy as np
from scipy.ndimage.filters import uniform_filter
from scipy.ndimage.measurements import variance


def conservative_smoothing_gray(data, filter_size):
    temp = []
    indexer = filter_size // 2
    new_image = data.copy()
    nrow, ncol = data.shape
    for i in range(nrow):
        for j in range(ncol):
            for k in range(i - indexer, i + indexer + 1):
                for m in range(j - indexer, j + indexer + 1):
                    if (k > -1) and (k < nrow):
                        if (m > -1) and (m < ncol):
                            temp.append(data[k, m])
            temp.remove(data[i, j])
            max_value = max(temp)
            min_value = min(temp)
            if data[i, j] > max_value:
                new_image[i, j] = max_value
            elif data[i, j] < min_value:
                new_image[i, j] = min_value
            temp = []
    return new_image.copy()


img = cv2.imread('/home/luolu/PycharmProjects/ParticleDetection/data/bp_src3/5.jpg')
height, width, channels = img.shape
src = cv2.GaussianBlur(img, (5, 5), 0)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary_ = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)

# 使用开运算去掉外部的噪声
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
binary = cv2.morphologyEx(binary_, cv2.MORPH_OPEN, kernel)
new_image = conservative_smoothing_gray(binary, 5)
compare = np.concatenate((binary, new_image), axis=1)  # side by side comparison

cv2.imshow('img', compare)
cv2.waitKey(0)
cv2.destroyAllWindows()
