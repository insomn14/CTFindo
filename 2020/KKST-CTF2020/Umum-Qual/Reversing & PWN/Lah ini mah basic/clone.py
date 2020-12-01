import random
from base64 import b64encode

def sstt(x):
    t = ''
    k = random.randint(1,6000)
    s = random.randint(0,6000)
    for c in x:
        t += chr(ord(c)-k^s)

    return b64encode(t.encode('utf-8'))


flag = "flag_lupa_to_delete_ayo_cepat_submit_!"
crypt_flag = sstt(flag)
print(crypt_flag)