from string import printable
import string, random

alphabet = dict(zip([x for x in range(len(string.printable[:-6]))],[x for x in string.printable[:-6]]))

def get_key(val):
    for key, value in alphabet.items():
         if val == value:
             return key

def i_am_a_ffine(plaintext, k1, k2):
    return ''.join(tuple(map(lambda x: alphabet[(k1 * int(get_key(x)) + k2) % 94], plaintext)))


def find_k1_k2(know, cipher):
    for k1 in range(1,94, 2):
        for k2 in range(0,94):
            tmp = i_am_a_ffine(know, k1, k2)
            if tmp == cipher:
                return k1,k2 # (15, 62)


flag = 'KKST2020{'
enc = open('enc.txt', 'r').read().strip()

k1, k2 = find_k1_k2(flag, enc[:len(flag)])

# exit(print(k1,k2))
while (len(flag) != len(enc)):
    for f in enc[len(flag):]:
        for c in printable[:-6]:
            ch = alphabet[(k1 * int(get_key(c)) + k2) % 94]
            if ch == enc[len(flag)]:
                flag += c
                break
print(flag)
