#!/usr/bin/python3
from pwn import *

r = remote('140.82.48.126',50002)

bangun = ['persegi','p-panjang','trapesium','segitiga']

try:
	while True:
		stri 	 = str(r.recvuntil(":"))
		checkbgn = [x for x in bangun if x in stri][0]
		checkbgn = checkbgn[0]
		numbs	 = [int(x) for x in stri.split(' ') if x.isdigit()]
		oper = 0 if "luasnya" in stri else 1
		res = 0
		if checkbgn =="persegi":
			if oper == 0:
				res = numbs[0]*numbs[0]
			else:
				res = 4*numbs[0]
		elif checkbgn == "p-panjang":
			if oper == 0:
				res = numbs[0]*numbs[1]
			else:
				res = (2*numbs[0]) + (2*numbs[1])
		elif checkbgn == "trapesium":
			if oper ==0:
				res = (numbs[0]+numbs[1]) * numbs[2]
			else:
				print("KEL TRAPESIUM BRE")
				break
		elif checkbgn == "segitiga":
			if oper==0:
				res = numbs[0]*numbs[1]*0.5
			else:
				print("KEL SEGITIGA BRE")
				break
		else:
			print("-"*40)
			print("INVALID SOAL")
			print(f"STRI 	 : {stri}")
			print(f"CHECKBGN : {checkbgn}")
			print(f"NUMBS	 : {numbs}")
			print(f"OPER : {oper}")
			break
		r.sendline(str(res))
except:
	print("INVALID - SOAL")
	print(f"STRI 	 : {stri}")
	print(f"CHECKBGN : {checkbgn}")
	print(f"NUMBS	 : {numbs}")
	print(f"OPER : {oper}")	
