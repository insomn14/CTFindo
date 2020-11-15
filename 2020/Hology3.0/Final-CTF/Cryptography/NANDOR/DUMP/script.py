#!/usr/bin/env python
# python 3.8

import cv2
from generator import genImage


def encrypt(gambar, kunci, params=0):
    imgOrKey = cv2.bitwise_or(gambar, kunci)
    imgAndKey = cv2.bitwise_and(gambar, kunci)
    notImgNKey = cv2.bitwise_not(imgAndKey)
    res = cv2.bitwise_and(imgOrKey, notImgNKey)

    if (params):
        cv2.imwrite('nandor/imgOrKey.png', imgOrKey)
        cv2.imwrite('nandor/imgAndKey.png', imgAndKey)

    return res


def main():
    genImage()

    flag = cv2.imread("flag.png")
    key0 = cv2.imread("key_00.png")
    key1 = cv2.imread("key_01.png")
    img0 = cv2.imread("img0.png")

    first = encrypt(img0, key0, 1)
    second = encrypt(flag, key1)
    third = encrypt(first, second)

    cv2.imwrite('nandor/flag_enc.png', third)
    paaneeh(img0, key1)


def paaneeh(a, b):  # iseng2
    dualK = encrypt(a, b)
    cv2.imwrite('nandor/apaini.png', dualK)


if __name__ == '__main__':
    import sys
    status = main()
    sys.exit(status)
