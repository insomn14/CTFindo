flag = ''
# part 1
part1 = 'hology3{'

# part 2
xoring = lambda cipher, key: ''.join(chr(c ^ key) for c in cipher.encode())
part2 = xoring('o|g', 9)

# part 3
part3 = 'th3'

# part 4
from z3 import Solver, BitVec, BV2Int, And, sat

s = Solver()
v = [BitVec(f'v_{i}',8) for i in range(6)]

s.add(And(
	v[0] + v[5] + v[4] + v[3] + v[2] + v[1] == 495,
	v[5] * 3 == 327,
	v[4] == v[5] - 58,
	v[2] + v[3] == 194,
	v[3] * v[2] == 9048,
	v[5] - v[0] == 33
	))

if s.check() == sat:
	mod = s.model()
	part4 = ''.join(chr(int(str(mod.evaluate(v[j])))) for j in range(6))[::-1]

# part 5
s = Solver()
v = [BitVec(f'v_{i}', 16) for i in range(5)]

s.add(And(
	BV2Int(v[2]) + BV2Int(v[4]) == 41177,
	BV2Int(v[2]) > BV2Int(v[4]),
	BV2Int(v[2]) * BV2Int(v[4]) == 2590182,
	v[0] == ord('c'),
	v[1] == ord('h'),
	v[3] == ord('n')
	))

if s.check() == sat:
	mod = s.model()
	part5 = ''.join(chr(int(str(mod.evaluate(v[j])))) if j not in [2,4] else str(mod.evaluate(v[j])) for j in range(5))

flag += part1 + part2 + '_' + part3 + '_' + part4 + '_' + part5 + '}'

print(flag)
