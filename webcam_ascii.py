import cv2
import numpy as np

cap = cv2.VideoCapture(0)
_, origin_img = cap.read()
origin_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)

origin_imax, origin_jmax = origin_img.shape
imax = 70
jmax = 200
img = np.zeros((imax, jmax))
charset = '@%#/+=-:. '

def average(i1, i2, j1, j2):
    avg = 0
    for i in range(i1, i2):
        for j in range(j1, j2):
            avg += origin_img[i][j]
    return avg // (len(range(i1, i2)) * len(range(j1, j2)))

def get_char(color):
    return color * (len(charset) - 1) // 255

def to_ascii(img):
    return [[charset[get_char(img[i][j])] for j in range(len(img[0]))] for i in range(len(img))]

while True:
    _, origin_img = cap.read()
    origin_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
    img = [[average(origin_imax * i // imax, origin_imax * (i + 1) // imax, origin_jmax * j // jmax, origin_jmax * (j + 1) // jmax) for j in range(jmax)] for i in range(imax)]
    ascii_img = "\n".join(["".join(x) for x in to_ascii(img)])
    print(ascii_img)

cap.release()
cv2.destroyAllWindows()
