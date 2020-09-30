from z3 import *

inp = [BitVec(f'v{i}', 8) for i in range(26)]
s = Solver()

s.add ( inp[5] == ord('-'), inp[11] == ord('-'), inp[18] == ord('-') )
s.add ( inp[0] == inp[10] )
s.add ( inp[1] == ord('e') )
s.add ( inp[3] == ord('P') )
s.add ( inp[25] == ord('Y'))
s.add ( inp[2] == ord('m') )
s.add ( inp[4] == inp[1] )
s.add ( inp[6] == ord('j') )
s.add ( inp[7] == ord('o') )
s.add ( inp[8] == inp[9] )
s.add ( inp[9] == ord('S') )
s.add ( inp[12] == (inp[5] * 2 + 9) )
s.add ( inp[23] == inp[17] + 3 )
s.add ( inp[13] == inp[20] )
s.add ( inp[14] == ord('z') )
s.add ( inp[16] == (inp[15] * 2 + 0xffffff7a) )
s.add ( inp[21] == ord('T') )
s.add ( inp[16] == ord('H') )
s.add ( inp[20] == ord('u') )
s.add ( inp[17] == ord('5') )
s.add ( inp[19] == ord('S') )
s.add ( inp[22] == ord('1') )
s.add ( inp[10] == inp[21] )
s.add ( inp[24] == (inp[20] * 2 + 0xffffffc3) )

if (s.check() == sat):
	model = s.model()
	res = [chr(int(str(model.evaluate(inp[i])))) for i in range(26)]
	print(''.join(res))
else:
	print('unsat')