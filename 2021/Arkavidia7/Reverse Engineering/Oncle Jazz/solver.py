mapping = {
	'a': 'u', 'b': '{', 'c': 'p', 'd': 'k', 'e': 'm', 'f': 'f', 'g': 'z', 'h': 'q', 'i': '}', 'j': 't', 'k': 'h', 'l': 'j', 'm': 's', 'n': 'y', 'o': 'o', 'p': '_', 'q': 'r', 'r': 'v', 's': 'l', 't': 'b', 'u': 'a', 'v': 'n', 'w': 'w', 'x': 'x', 'y': 'i', 'z': 'e', '_': 'g', '{': 'd', '}': 'c'
	}
from pwn import xor

k = b'oncle'
part1 = xor(bytes.fromhex('0A0B3C011B3A090E010C0909141558130D081C2E')[::-1], k).decode('utf-8')

stack = 'pyogzyuj'[::-1]
stack += 'jmgtueeeeeec'
part2 = ''
while len(part2) != len(stack):
	for m in mapping.keys():
		if mapping[m] == stack[len(part2)]:
			part2 += m
print(part1+part2)
