#!/usr/bin/env python
# python 3.8

import numpy
from PIL import Image


def genImage(width=500, height=400, num_of_images=2):
    width = int(width)
    height = int(height)
    num_of_images = int(num_of_images)

    for n in range(num_of_images):
        filename = f'key_{n:02d}.png'
        rgb_array = numpy.random.rand(height, width, 3) * 255
        image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')
        image.save(filename)
