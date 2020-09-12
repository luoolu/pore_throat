# -*- coding: utf-8 -*-
# @Time : 2020/4/2 下午2:35
# @Author : LuoLu
# @FileName: bilateral_filtering.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/luolu/PycharmProjects/ParticleDetection/data/bp_src3/5.jpg')
# Blur the image
img_0 = cv2.blur(img, ksize=(7, 7))
img_1 = cv2.GaussianBlur(img, ksize=(7, 7), sigmaX=0)
img_2 = cv2.medianBlur(img, 17)
img_3 = cv2.bilateralFilter(img, 31, sigmaSpace=75, sigmaColor=75)
# Plot the images
compare = np.concatenate((img, img_1), axis=1) #side by side comparison
compare2 = np.concatenate((img, img_2), axis=1) #side by side comparison
compare3 = np.concatenate((img, img_3), axis=1) #side by side comparison

cv2.imshow('GaussianBlur', compare)
cv2.imshow('medianBlur', compare2)
cv2.imshow('bilateralFilter', compare3)
cv2.waitKey(0)
cv2.destroyAllWindows()
