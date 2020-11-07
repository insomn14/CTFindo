import imagehash 
import numpy as np
import os, time, random
from PIL import Image
from cv2 import imread, imwrite, bitwise_xor
from Crypto.Util.number import bytes_to_long


def decrypt(keypath, key):
	kunci = imread(keypath)
	harta_enc = imread(".harta_enc.png")
	dec = bitwise_xor(kunci, harta_enc)
	imwrite(f"harta_dec_{key}.png", dec)

def encrypt(keypath, key):
	kunci = imread(keypath)
	harta = imread("harta.png")
	encrypted = bitwise_xor(kunci, harta)
	imwrite(f"harta_enc_{key}.png", encrypted)


for i in range(10):
	key = f'20200929225324/key_candidate_0{i}.png'
	decrypt(key, i)
