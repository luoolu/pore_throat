# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 下午4:10
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : img2logic.py
# @Software: PyCharm

import cv2
import numpy as np

img1 = cv2.imread('/home/luolu/Downloads/data/yashi_bp/pore_throat_img/add_cleaned_single1.png')
img2 = cv2.imread('/home/luolu/Downloads/data/yashi_bp/pore_throat_img/colored_pore_single1.png')
# img1 = cv2.imread('/home/luolu/Downloads/data/yashi_bp/pore_throat_img/cleaned_single1.png')
# img2 = cv2.imread('/home/luolu/Downloads/data/yashi_bp/pore_throat_img/Single_1.png')


subtract = cv2.subtract(img1, img2)
add = cv2.add(img1, img2)
bitwise_xor = cv2.bitwise_not(img1, img2)
bitwise_and = cv2.add(img1, img2)


cv2.imwrite("/home/luolu/Downloads/data/yashi_bp/pore_throat_img/add_accp_single1.png", add)


# cv2.imshow('subtract', subtract)
# cv2.imshow('add', add)
# cv2.imshow('bitwise_xor', bitwise_xor)
# cv2.imshow('bitwise_and', bitwise_and)

cv2.waitKey(0)
cv2.destroyAllWindows()