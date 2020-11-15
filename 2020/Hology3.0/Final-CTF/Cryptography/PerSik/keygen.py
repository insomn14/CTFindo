import random

key = []
for i in range(1000):
    key.append(i)
random.shuffle(key)
key_out = ""
key_out += str(key[0])
for i in range(1, 1000):
    key_out += ", " + str(key[i])
open('key', 'w').write(key_out)