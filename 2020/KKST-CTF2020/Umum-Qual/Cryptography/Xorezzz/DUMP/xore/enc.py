import sys
from struct import pack, unpack
from random import randint
import gmpy2

n = 1007621497415251
m = 625346600

def HhH(w):
	return ((w * 7331 >> 16) ^ (w * 20202) ) % 4294967296

def encrypt(block):
	zz, z, zzzz, zzz = unpack("<4I", block)
	for rno in xrange(1337):
		zz, z, zzzz, zzz = z ^ HhH(zz | HhH(zzzz ^ HhH(zzz)) ^ HhH(zz | zzzz) ^ zzz), zzzz ^ HhH(zz ^ HhH(zzz) ^ (zz | zzz)), zzz ^ HhH(zz | HhH(zz) ^ zz), zz ^ 20202
		zz, z, zzzz, zzz = zzzz ^ HhH(zzz | HhH(z ^ HhH(zz)) ^ HhH(zzz | z) ^ zz), z ^ HhH(zzz ^ HhH(zz) ^ (zzz | zz)), zz ^ HhH(zzz | HhH(zzz) ^ zzz), zzz ^ 7331
	return pack("<4I", zz, z, zzzz, zzz)

def encrypt_again(flag):
    ciphertext = []
    plaintext = ''.join([bin(ord(i))[2:].zfill(8) for i in flag])
    for b in plaintext:
        e = randint(1, n)
        c = pow(m, e, n)
        if b == '1':
            ciphertext.append(c)
        else:
            c = -c % n
            ciphertext.append(c)
    return ciphertext


pt="KKST2020{sambit_gan}"
while len(pt) % 16: pt += "F"
ct = [encrypt(pt[i:i+16]).encode('hex') for i in xrange(0, len(pt), 16)]
ctx=[]
for i in ct:
    ctx+=encrypt_again(i)
ctx.append(m)
f=open("enc1.txt","w")
f.write(str(ctx))
f.close()