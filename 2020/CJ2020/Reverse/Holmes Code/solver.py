#!/usr/bin/python3

from z3 import *
import re

def main():
	data = open('data.txt', 'r').read()

	cal = [int(i,16) for i in re.findall(r'80\s(?!fa)\w+\s(\w+)', data)]
	cmp = [int(i,16) for i in re.findall(r'fa\s+(\w+)', data)]
	opr = [i for i in re.findall(r'add|sub|xor', data)]

	data = ''
	for i, o in enumerate(opr):
		s = Solver()
		inp = BitVec('inp',8)

		if o == 'sub':
			s.add(inp - cal[i] == cmp[i])
		elif o == 'add':
			s.add(inp + cal[i] == cmp[i])
		elif o == 'xor':
			s.add(inp ^ cal[i] == cmp[i])

		if s.check() == sat:
			model = s.model()
			res = chr(int(str(model[inp])))
			data += res
	print(data)

if __name__ == '__main__':
	main()