from math import sqrt

rbp_4 = 10
rbp_8 = 8
rbp_12 = 5875
rbp_16 = 19

#-----------------------
eax = rbp_4 * rbp_8
eax += eax
edi = eax
eax = int(sqrt(edi))
rbp_20 = eax
#-----------------------
eax = rbp_4 * rbp_16
eax += eax
edi = eax
eax = int(sqrt(edi))
rbp_24 = eax
#-----------------------
eax = rbp_12 * rbp_20
rbp_28 = eax
eax = rbp_12 * rbp_24
rbp_32 = eax
eax = rbp_32 - rbp_28
rbp_36 = eax
eax = rbp_36 * eax
rbp_36 = eax

if (rbp_36 < rbp_32): # jle .L2
    if (rbp_36 > rbp_32): # jge .L3
        print('exit')
    eax = (rbp_36 | 17081945) + 177013
    rbp_36 = eax
    print(eax)
    print('JLE')
else:
    eax = (rbp_36 | 19450817) + 177013
    print(eax)
    print('ELSE')
print('FINISH')
