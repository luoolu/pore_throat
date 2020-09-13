# -*- coding: utf-8 -*-
# @Time : 2020/3/4 上午10:15
# @Author : LuoLu
# @FileName: ColorDetection.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com

from __future__ import division
import cv2
import numpy as np


def nothing(*arg):
    pass


# Initial HSV GUI slider values to load on program start.
# icol = (36, 202, 59, 71, 255, 255)  # Green
# icol = (18, 0, 196, 36, 255, 255)  # Yellow
# icol = (0, 100, 80, 10, 255, 255)   # Red
# icol = (0, 100, 80, 10, 255, 255)   # Red
# icol = (89, 0, 0, 125, 255, 255)  # light Blue 0, 255, 255
# icol = (1, 10, 99, 10, 150, 255)   # fen R: 254 G: 195 B: 180 | 255, 192, 192
# icol = (0, 136, 126, 176, 255, 200)   # caolv R: 0 G: 136 B: 126 | 0, 128, 128
# icol = (160, 80, 45, 190, 150, 255)   # shenzi R: 126 G: 126 B: 255
# icol = (150, 150, 200, 255, 255, 255)   # light_fen
# icol = (1, 10, 99, 10, 150, 255)  # Quartz 石英	255, 192, 192
# icol = (0, 255, 255, 50, 255, 255)  # Albite 钠长石	0, 255, 255
# icol = (0, 128, 128, 50, 200, 200)  # K-Feldspar 钾长石	0, 128, 128
# icol = (192, 192, 255, 220, 220, 255)  # Calcite 方解石	192, 192, 255
# icol = (128, 128, 255, 180, 180, 255)  # Dolomite 白云石	128, 128, 255
# icol = (192, 64, 0, 235, 128, 50)  # Kaolinite 高岭石	192, 64, 0
# icol = (0, 192, 0, 50, 235, 50)  # Illite 伊利石	0, 192, 0
# icol = (0, 255, 0, 50, 255, 50)  # Chlorite 绿泥石	0, 255, 0
# icol = (0, 64, 0, 50, 120, 50)  # Muscovite 云母	0, 64, 0
# icol = (51, 102, 0, 100, 160, 50)  # Smectite 蒙脱石	51, 102, 0
# icol = (255, 255, 0, 255, 255, 100)  # Pyrite 黄铁矿	255, 255, 0
# icol = (224, 224, 224, 255, 255, 255)  # Pores 孔隙	224, 224, 224
icol = (0, 0, 0, 255, 255, 255)  # Unclassified 无法识别的	18, 0, 159, 175, 255, 255

cv2.namedWindow('colorTest', flags=2)
# Lower range colour sliders.
cv2.createTrackbar('lowHue', 'colorTest', icol[0], 255, nothing)
cv2.createTrackbar('lowSat', 'colorTest', icol[1], 255, nothing)
cv2.createTrackbar('lowVal', 'colorTest', icol[2], 255, nothing)
# Higher range colour sliders.
cv2.createTrackbar('highHue', 'colorTest', icol[3], 255, nothing)
cv2.createTrackbar('highSat', 'colorTest', icol[4], 255, nothing)
cv2.createTrackbar('highVal', 'colorTest', icol[5], 255, nothing)

# Raspberry pi file path example.
# frame = cv2.imread('/home/pi/python3/opencv/color-test/colour-circles-test.jpg')
# Windows file path example.
frame = cv2.imread('/home/luolu/Downloads/data/yashi_bp/pore_throat_img/pore_extract_10Xcrop/16-0460_5.png')

while True:
    # Get HSV values from the GUI sliders.
    lowHue = cv2.getTrackbarPos('lowHue', 'colorTest')
    lowSat = cv2.getTrackbarPos('lowSat', 'colorTest')
    lowVal = cv2.getTrackbarPos('lowVal', 'colorTest')
    highHue = cv2.getTrackbarPos('highHue', 'colorTest')
    highSat = cv2.getTrackbarPos('highSat', 'colorTest')
    highVal = cv2.getTrackbarPos('highVal', 'colorTest')

    # Show the original image.
    cv2.imshow('frame', frame)

    # Blur methods available, comment or uncomment to try different blur methods.
    frameBGR = cv2.GaussianBlur(frame, (7, 7), 0)
    # frameBGR = cv2.medianBlur(frameBGR, 7)
    # frameBGR = cv2.bilateralFilter(frameBGR, 15 ,75, 75)
    """kernal = np.ones((15, 15), np.float32)/255
    frameBGR = cv2.filter2D(frameBGR, -1, kernal)"""

    # Show blurred image.
    cv2.imshow('blurred', frameBGR)

    # HSV (Hue, Saturation, Value).
    # Convert the frame to HSV colour model.
    hsv = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2HSV)

    # HSV values to define a colour range.
    colorLow = np.array([lowHue, lowSat, lowVal])
    colorHigh = np.array([highHue, highSat, highVal])
    mask = cv2.inRange(hsv, colorLow, colorHigh)
    # Show the first mask
    cv2.imshow('mask-plain', mask)

    kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

    # Show morphological transformation mask
    cv2.imshow('mask', mask)

    # Put mask over top of the original image.
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Show final output image
    cv2.imshow('colorTest', result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
