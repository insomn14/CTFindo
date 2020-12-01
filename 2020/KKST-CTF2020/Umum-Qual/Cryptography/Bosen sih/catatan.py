from Crypto.Util.number import *
import gmpy2

flag = "KKST2020{Sumpah_Nek_Awakmu_submit_iki_gendeng_lan_edan}" 
#duduk flag / bukan flag / NOTF FLAG

p0 = getPrime(512)
q0 = getPrime(512)
while gmpy2.gcd((p0-1)*(q0-1),100)!=4:
    p0 = getPrime(512)
    q0 = getPrime(512)

p1 = getPrime(512)
q1 = getPrime(512)
p2 = getPrime(512)
q2 = getPrime(512)
p3 = gmpy2.next_prime(p1)
q3 = gmpy2.next_prime(q1)
p4 = gmpy2.next_prime(p2)
q4 = gmpy2.next_prime(q2)
p5 = getPrime(1024)
q5 = getPrime(1024)
p6 = getPrime(1024)
q6 = getPrime(1024)
p7 = getPrime(1024)
q7 = getPrime(1024)

e = 65537
n1 = p1*p3*q1*q3 # <- broadcast attack 
n2 = p2*p4*q2*q4 # <- broadcast attack 
n3 = p5*q6
n4 = p6*q5
n5 = p7*q7
n6 = p0*q0

phi1 = (p1-1)*(p3-1)*(q1-1)*(q3-1)
phi2 = (p2-1)*(p4-1)*(q2-1)*(q4-1)
d1 = gmpy2.invert(e,phi1)
d1 = gmpy2.invert(e,phi2)

c1 = pow(bytes_to_long(flag[0:23]),e,n1)
c1 = pow(c1,e,n1)
c1 = pow(c1,e,n1) # <- result

c2 = pow(bytes_to_long(flag[23:46]),e/655,n6)
c2 = pow(c2,e,n2)
c2 = pow(c2,e,n2)
c2 = pow(c2,e,n2) # <- result

c3 = pow(c2,e//21779,n3) # 3 <- lowest exponent attack
c4 = pow(c2,e//21779,n4) # 3 <- lowest exponent attack
c5 = pow(c2,e//21779,n5) # 3 <- lowest exponent attack

print "eq1 =",pow(p1+q3,65537,n1)
print "eq2 =",pow(p3+q1,65537,n1)
print "eq3 =",pow(p2+q4,65537,n2)
print "eq4 =",pow(p4+q2,65537,n2)

print "eq5 =",pow(p0,e/65537,n6) # print value p0
print "eq6 =",pow(q0,e/65537,n6) # print value q0

print "n1 =",n1 
print "n2 =",n2
print "n3 =",n3
print "n4 =",n4
print "n5 =",n5

print "c1 =",c1
print "c3 =",c3
print "c4 =",c4
print "c5 =",c5

'''
*Note:
	# Found p0, q0 and n6 
	eq5 -> p0
	eq6 -> q0
	n6 -> p0*q0





'''