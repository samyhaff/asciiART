import cv2
import numpy as np
import sys

origin_img = cv2.imread('marc.jpg', cv2.IMREAD_GRAYSCALE)

origin_imax, origin_jmax = origin_img.shape
imax = 100
jmax = 300
img = np.zeros((imax, jmax))

def average(i1, i2, j1, j2):
    avg = 0
    for i in range(i1, i2):
        for j in range(j1, j2):
            avg += origin_img[i][j]
    return avg // (len(range(i1, i2)) * len(range(j1, j2)))

img = [[average(origin_imax * i // imax, origin_imax * (i + 1) // imax, origin_jmax * j // jmax, origin_jmax * (j + 1) // jmax) for j in range(jmax)] for i in range(imax)]

charset = '@%#/+=-:. '

def get_char(color):
    return color * (len(charset) - 1) // 255

def to_ascii(img):
    return [[charset[get_char(img[i][j])] for j in range(len(img[0]))] for i in range(len(img))]

ascii_img = "\n".join(["".join(x) for x in to_ascii(img)])
print(ascii_img)
