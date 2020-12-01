import hashlib


def md5(s):
	return hashlib.md5(s.encode('utf-8')).hexdigest()


def bapack(a, b, c):
    from random import choice,randint
    r = ''
    s = b
    h = randint(0,30)
    n = randint(0,30)
    for p in a:
        if p not in c:
            r += p
            continue
        x = c[(c.index(p) + s + h) % n]
        r += x
        s = c.index(p)
    return r


#destroy the key
def bacpak(k):
	for x in k:
		print(md5(x))


def signedFlag(f):
	f = f
	for x in range(1000):
		f = md5(f)
		print(f)
	print(f) #9b9b6a18109487408288e091ecdb13d2


exit(0)

flag = ""
key  = ""
key2 = 0
print(signedFlag(flag))
print(bapack(flag, key2, key))


#destroyed key
# 3a3ea00cfc35332cedf6e5e9a32e94da
# e358efa489f58062f10dd7316b65649e
# 4a8a08f09d37b73795649038408b5f33
# 5dbc98dcc983a70728bd082d1a47546e
# 7694f4a66316e53c8cdd9d9954bd611d
# 83878c91171338902e0fe0fb97a8c47a
# 415290769594460e2e485922904f345d
# 4b43b0aee35624cd95b910189b3dc231
# 865c0c0b4ab0e063e5caa3387c1a8741
# 61e9c06ea9a85a5088a499df6458d276
# 03c7c0ace395d80182db07ae2c30f034
# a5f3c6a11b03839d46af9fb43c97c188
# 9dd4e461268c8034f5c8564e155c67a6
# 2db95e8e1a9267b7a1188556b2013b33
# ff44570aca8241914870afbc310cdb85
# d95679752134a2d9eb61dbd7b91c4bcc
# e1671797c52e15f763380b45e841ec32
# c1d9f50f86825a1a2302ec2449c17196
# 9d5ed678fe57bcca610140957afab571
# b9ece18c950afbfa6b0fdbfa4ff731d3
# 69691c7bdcc3ce6d5d8a1361f22d04ac
# 8fa14cdd754f91cc6554c9e71929cce7
# 7b8b965ad4bca0e41ab51de7b31363a1
# f09564c9ca56850d4cd6b3319e541aee
# 8277e0910d750195b448797616e091ad
# dd7536794b63bf90eccfd37f9b147d7f
# 

#encrypyted flag
#AKSaP3Jg!K@d@Wf3l5?drhpAwtaT1qC3HluEUMfffPaKky4H@mP4CkXnfX0
