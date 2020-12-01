from z3 import BitVec, Solver, sat, And, Or
from base64 import b64decode

def is_valid(x):
	#  ascii_letters + digits + '}_!@{'
	return Or((x == 97 ), (x == 98 ), (x == 99 ), (x == 100 ), (x == 101 ), (x == 102 ), (x == 103 ), (x == 104 ), (x == 105 ), (x == 106 ), (x == 107 ), (x == 108 ), (x == 109 ), (x == 110 ), (x == 111 ), (x == 112 ), (x == 113 ), (x == 114 ), (x == 115 ), (x == 116 ), (x == 117 ), (x == 118 ), (x == 119 ), (x == 120 ), (x == 121 ), (x == 122 ), (x == 65 ), (x == 66 ), (x == 67 ), (x == 68 ), (x == 69 ), (x == 70 ), (x == 71 ), (x == 72 ), (x == 73 ), (x == 74 ), (x == 75 ), (x == 76 ), (x == 77 ), (x == 78 ), (x == 79 ), (x == 80 ), (x == 81 ), (x == 82 ), (x == 83 ), (x == 84 ), (x == 85 ), (x == 86 ), (x == 87 ), (x == 88 ), (x == 89 ), (x == 90 ), (x == 48 ), (x == 49 ), (x == 50 ), (x == 51 ), (x == 52 ), (x == 53 ), (x == 54 ), (x == 55 ), (x == 56 ), (x == 57 ), (x == 95 ), (x == 33 ), (x == 64 ), (x == 32),(x == 33), (x == 34), (x == 35), (x == 36), (x == 37), (x == 38), (x == 39), (x == 40), (x == 41), (x == 42), (x == 43), (x == 45), (x == 46), (x == 47), (x == 59), (x == 60), (x == 61), (x == 62), (x == 63), (x == 64), (x == 91), (x == 92), (x == 93), (x == 94), (x == 95), (x == 96), (x == 123), (x == 125), (x == 126))


enc = b64decode(open('output.txt', 'r').read().strip()).decode('utf-8')
inp = [BitVec(f'inp_{i}',8) for i in range(len(enc))]
k = BitVec('k',8)
s = BitVec('s',8)
S = Solver()


S.add(Or(k > 1, k <= 6000))
S.add(Or(s > 0, s <= 6000))

for n in range(len(inp)):
	S.add(is_valid(inp[n]))

for i in range(len(enc)):
	S.add(inp[i]-k^s == ord(enc[i]))
	

if S.check() == sat:
	model = S.model()
	flag = ''.join(chr(int(str(model[inp[i]]))) for i in range(len(inp)))
	print(f'k : {model[k]}')
	print(f's : {model[s]}')
	print(f'FLAG : KKST2020{flag[::-1]}')
else:
	print('unsat')
