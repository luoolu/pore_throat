# -*- coding: utf-8 -*-
# @Time : 2020/4/2 下午2:10
# @Author : LuoLu
# @FileName: Gaussian_fielter.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com
import cv2
import numpy as np

img = cv2.imread('/home/luolu/PycharmProjects/ParticleDetection/data/bp_src3/5.jpg')
new_image = cv2.GaussianBlur(img, (5, 5), 0)
# median = cv2.medianBlur(img, 5)
compare = np.concatenate((img, new_image), axis=1) #side by side comparison

cv2.imshow('img', compare)
cv2.waitKey(0)
cv2.destroyAllWindows()





