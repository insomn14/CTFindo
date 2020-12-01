from string import ascii_lowercase
import random

cmpr = 1995
sepr = [4,9,14]
crack = lambda x: sum([ord(c) for c in x])


while(True):
    tmp = ''.join(random.choice(ascii_lowercase) if i not in sepr else '-' for i in range(19))
    if crack(tmp) == cmpr:
        print(f'Found: {tmp}')
        break

