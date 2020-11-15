import re
import random

enckey = open('key', 'r').read()
strKey = re.split(', ', enckey)
mapObject = map(int, strKey)
key = list(mapObject)
fileName = input('Enter file name:')
plaintext = open(fileName, 'r').read()
ciphertext = ""
lowestIn = 0
last = -1

for i in range(len(plaintext)):
    lowest = min(x for x in key[0:len(plaintext)] if x > last)
    for i in range(len(plaintext)):
        if key[i] == lowest:
            lowestIn = i
            break
    ciphertext += plaintext[lowestIn]
    last = key[lowestIn]

fileName = ""
for i in range(4):
    fileName += str(random.randint(0,9))
fileName += ".txt"
open(fileName, 'w').write(ciphertext)