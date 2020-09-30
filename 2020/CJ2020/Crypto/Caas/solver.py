#!/usr/bin/python
from Crypto.Util.number import bytes_to_long as btl
from Crypto.Util.number import long_to_bytes as ltb
from base64 import b64decode
from Crypto.Cipher import AES
from pwn import *

host, port = 'net.cyber.jawara.systems', 3001

r = remote(host, port)

pack = '\x00'*64

print(r.recvline())
r.sendline(pack)

print(r.recvuntil(':\n'))

leak = b64decode(r.recvline().strip())
log.info('INPUT : {}'.format(btl(leak)))

iv = leak
enc_flag = b64decode('pJ8GmKrvZS0dO3LPfcvjXrbIRusaEF/wb/Ps8ENwmH0fvkcIau74mSnZPwBvbyMeXyUrAvDBY+McaztsZsM+nw==')
log.info('IV : {}'.format(btl(iv)))
log.info('ENC FLAG : {}'.format(btl(enc_flag)))

a1 = xor(enc_flag,iv)
print(a1)


r.interactive()