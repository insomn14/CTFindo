import binascii
from Crypto.Cipher import AES

KEY_first = "1niL0HkuNc1NY4"
cipher1 = "1a00000000000000000000000000006a"
cipher2 = "b22c40003a49dbf8d8e6f49fb141e030"

plain1 = "hology3{paan_neh"
plain2 = "_binun_aqu} != f"

def decrypt(cipher, passphrase, cp=binascii.unhexlify(cipher1)):
	aes = AES.new(passphrase, AES.MODE_CBC, cp)
	return aes.decrypt(cipher)

def trying_key(Key):
	tmp = binascii.hexlify(decrypt(binascii.unhexlify(cipher2), Key, cp=plain2))
	if tmp[:2] == '1a' and tmp[-2:] == '6a':
		print('FOUND : {}'.format(tmp)) 
		print('KEY : {}'.format(Key))
		exit()

for i in range(30, 127):
	for j in range(30, 127):
		key = KEY_first + chr(i) + chr(j)
		dec_plain2 = decrypt(binascii.unhexlify(cipher2),  key)
		if  str(dec_plain2).startswith("_") and str(dec_plain2).endswith('f'):
			# print("Found key: {}".format(key))
			trying_key(key)