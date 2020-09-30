from PIL import Image
from numpy import *

one_img = Image.open(r'pix.png')

one = array(one_img)

a, b, c = one.shape
#print(img.shape)

data = ''
for x in range(0, a):
    for y in range(0, b):
        pixel1 = one[x, y]
        for px in pixel1:
        	data += chr(px)

print(data)
