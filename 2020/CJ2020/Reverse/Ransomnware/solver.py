#!/usr/bin/python3

val = []
a1, a2 = 0, 0
enc_flag = open('flag.txt.enc', 'rb').read().strip()
stk_rand = [0x72, 0x68, 0x63, 0x6D, 0x65, 0x6D, 0x5F, 0x5F, 0x63, 0xAD, 0x65, 0x6D, 0x5F, 0x5F, 0xDA, 0x43]

xor = lambda x, y : bytearray(i^j for i,j in zip(x,y))

def fill():
	global val, a1, a2
	val = [i for i in range(256)] 
	a1, a2 = 0, 0

def get_value():
	global val,a1, a2
	a1 = (a1 + 1) % 256
	a2 = (a2 + val[a1]) % 256
	val[a1], val[a2] = val[a2], val[a1] # swap position
	return val[(val[a1] + val[a2]) % 256]

def procSwap(a1, a2):
	global val
	x = 0
	for i in range(256):
		try:
			x = (val[i] + x +  a1[i % a2]) % 256
		except ZeroDivisionError:
			x = (val[i] + x +  a1[0]) % 256
		val[i], val[x] = val[x], val[i] # swap position

def execute(Rand, FEnc):
	global val
	fill()											# create table array[256] 1..255
	procSwap(Rand, len(Rand))						# swap array position using stk_rand
	get = [get_value() for i in range(len(FEnc))]   # get 32 byte value from array table & swap position
	result = xor(FEnc, get)
	return result

if __name__ == '__main__':
	urand = execute(stk_rand, enc_flag[:32])		# recovery /dev/urandom
	flag = execute(urand, enc_flag[32:])				# recovery flag
	print(flag.decode('utf-8'))
