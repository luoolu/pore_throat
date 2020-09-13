# -*- coding: utf-8 -*-
# @Time : 2020/3/30 下午2:56
# @Author : LuoLu
# @FileName: batch_particle_detection.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com
from PIL import Image
import glob
import os

import cv2 as cv
import numpy as np
from PIL import Image
import numpy as np

# root_path = '/home/luolu/PycharmProjects/ParticleDetection/'
# first step, color space


if __name__ == '__main__':
    base_name = ''
    counter = 0
    for filename in sorted(glob.glob('/home/luolu/Downloads/data/yashi_bp/pore_throat_img/10X裁剪/*/*.png')):
        img = cv.imread(filename)
        height, width, channels = img.shape
        print(filename)
        base_name = os.path.basename(filename)
        # Blur methods available, comment or uncomment to try different blur methods.
        frameBGR = cv.GaussianBlur(img, (7, 7), 0)
        # frameBGR = cv2.medianBlur(frameBGR, 7)
        # frameBGR = cv2.bilateralFilter(frameBGR, 15 ,75, 75)
        """kernal = np.ones((15, 15), np.float32)/255
        frameBGR = cv2.filter2D(frameBGR, -1, kernal)"""

        # Show blurred image.
        # cv.imshow('blurred', frameBGR)

        # HSV (Hue, Saturation, Value).
        # Convert the frame to HSV colour model.
        hsv = cv.cvtColor(frameBGR, cv.COLOR_BGR2HSV)

        # HSV values to define a colour range. # 7, 0, 148, 140, 255, 255
        # colorLow = np.array([lowHue, lowSat, lowVal])
        # colorHigh = np.array([highHue, highSat, highVal])
        # 7, 0, 148, 140, 255, 255   white
        # 150, 108, 139, 255, 255, 255   red
        # 0, 0, 0, 125, 255, 255   white and hui
        # 15, 0, 161, 111, 255, 255   temp
        # 0, 0, 0, 255, 115, 255   temp
        # 0, 0, 0, 255, 84, 255   temp
        # 0, 0, 134, 255, 255, 255   temp
        colorLow = np.array([0, 0, 0])
        colorHigh = np.array([255, 128, 255])
        mask = cv.inRange(hsv, colorLow, colorHigh)
        # Show the first mask
        # cv.imshow('mask-plain', mask)

        kernal = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7, 7))
        mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)
        mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)


        # mask for black and white exchange --add for pore throat
        # mask = cv.subtract(255, mask)

        # Show morphological transformation mask
        # cv.imshow('mask', mask)
        # save
        # cv.imwrite(root_path + "data/bp_mask3/" + base_name, mask)

        # Put mask over top of the original image.
        result = cv.bitwise_and(img, img, mask=mask)
        # save
        cv.imwrite("/home/luolu/Downloads/data/yashi_bp/pore_throat_img/pore_extract_10Xcrop/" + base_name, result)
        # cv.imwrite(root_path + "data/yashi_qscan/src_image/" + base_name, result)
        # cv.imwrite("/home/luolu/Downloads/data/CT_wst/cropped_filter/" + base_name, result)
        # cv.imwrite("/home/luolu/Downloads/data/yashi_bp/pore_throat_img/mv_pore_Single_1.jpg", result)
        counter = counter + 1
    print('counter: ', counter)
