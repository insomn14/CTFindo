import hashlib
from string import printable

md5 = lambda s: hashlib.md5(s.encode('utf-8')).hexdigest()


def signedFlag(f):
	f = f
	for x in range(1000):
		f = md5(f)
	return f

def recovery(patrn, enc, key2, v_h, v_n, key):
	r = ''
	h = v_h
	n = v_n
	s = key2
	for i, en in enumerate(enc):
		if en != '-':
			r += en
			continue
		for c in key:
			try:
				x = key[(key.index(c) + s + h) % n]
				if x == patrn[i]:
					r += c
					s = key.index(c)
					break
			# print(r)
			except: pass
	return r

def bapack(flag, key2, v_h, v_n, key_recov):
	from random import randint
	r = ''
	s = key2
	h = v_h
	n = v_n
	for c_flag in flag:
		if c_flag not in key_recov:
			r += c_flag
			continue
		x = key_recov[ (key_recov.index(c_flag) + s + h) % n ]
		r += x
		s = key_recov.index(c_flag)
	return r

def find_key():
	list_key = ['3a3ea00cfc35332cedf6e5e9a32e94da',	'e358efa489f58062f10dd7316b65649e',	'4a8a08f09d37b73795649038408b5f33',	'5dbc98dcc983a70728bd082d1a47546e',	'7694f4a66316e53c8cdd9d9954bd611d',	'83878c91171338902e0fe0fb97a8c47a',	'415290769594460e2e485922904f345d',	'4b43b0aee35624cd95b910189b3dc231',	'865c0c0b4ab0e063e5caa3387c1a8741',	'61e9c06ea9a85a5088a499df6458d276',	'03c7c0ace395d80182db07ae2c30f034',	'a5f3c6a11b03839d46af9fb43c97c188',	'9dd4e461268c8034f5c8564e155c67a6',	'2db95e8e1a9267b7a1188556b2013b33',	'ff44570aca8241914870afbc310cdb85',	'd95679752134a2d9eb61dbd7b91c4bcc',	'e1671797c52e15f763380b45e841ec32',	'c1d9f50f86825a1a2302ec2449c17196',	'9d5ed678fe57bcca610140957afab571',	'b9ece18c950afbfa6b0fdbfa4ff731d3',	'69691c7bdcc3ce6d5d8a1361f22d04ac',	'8fa14cdd754f91cc6554c9e71929cce7',	'7b8b965ad4bca0e41ab51de7b31363a1',	'f09564c9ca56850d4cd6b3319e541aee',	'8277e0910d750195b448797616e091ad',	'dd7536794b63bf90eccfd37f9b147d7f']

	return ''.join(c for end in list_key for c in printable if md5(c) == end)


key = find_key()
# key -> 'EtcSqpyriWsKxlJoeHBTMfnQdI'
f_md5 = '9b9b6a18109487408288e091ecdb13d2'
f_enc = 'AKSaP3Jg!K@d@Wf3l5?drhpAwtaT1qC3HluEUMfffPaKky4H@mP4CkXnfX0'

f_know = ''.join(c if c not in key else '-' for c in f_enc) 
# f_know -> 'A--aP3-g!-@-@--3-5?--h-Aw-a-1-C3--u-U----Pa-k-4-@mP4CkX--X0'


for k2 in range(30):
	for h in range(30):
		for n in range(30):
			res = recovery(f_enc, f_know, k2, h, n, key)
			enc = bapack(res, k2, h, n, key)
			if (len(res) == len(f_know) and enc == f_enc) :
				cond = signedFlag(res) == f_md5
				print('-----------------------------[UPDATE]-----------------------------')
				print(f'STR_KEY : {key}')
				print(f'VAL_KEY2 : {k2}')
				print(f'VAL_H|N : {h}|{n}')
				print(f'ORI_PTR : {f_know}')
				print(f'ORI_EPT : {f_enc}')
				print(f'GEN_GET : {res}')
				print(f'GEN_ENC : {enc}')
				print(f'CHECK : {cond}')
				if (cond): exit(print('-----------------------------[FOUND]-----------------------------'))