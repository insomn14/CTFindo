import hashlib
from itertools import permutations, product

proximity = [150, 150, 300, 200, 220, 250]
velocity = [80, 70, 40, 90, 75, 60]
name = ['imp', 'demon', 'ogre', 'skeleton', 'swampy', 'zombie']
arkav = "아르카뷔디아"; # Arcavidia
mkilld = [None]*len(arkav)
# (mkilld[0].proximity * (mkilld[0].velocity + mkilld[0].name.charCodeAt(0) + 20))
for n,v,p in zip(name, velocity, proximity):
	tmp = p * (v + ord(n[0]) + 20)
	if tmp == ord(arkav[0]):
		print(n,v,p,tmp)
		mkilld[0] = [n,v,p]
# ((mkilld[1].name.charCodeAt(0) - 64).toString().repeat(2) + mkilld[1].proximity/50)
mkilld[1] = [name[2], velocity[2], proximity[2]]
# (Number(mkilld[2].proximity + "" + mkilld[2].velocity) * 2 + mkilld[2].name.charCodeAt(0) * 75 + 77)
for n,v,p in zip(name, velocity, proximity):
	tmp = (int(str(f'{p}{v}')) * 2)  + ord(n[0]) * 75 + 77
	if tmp == ord(arkav[2]):
		print(n,v,p,tmp)
		mkilld[2] = [n,v,p]
# (mkilld[3].name.charCodeAt(0) * mkilld[3].name.charCodeAt(1) * 4 + (mkilld[3].proximity + mkilld[3].velocity) * 16 - 864)
for n,v,p in zip(name, velocity, proximity):
	tmp = (ord(n[0]) * ord(n[1]) * 4 + (p + v) * 16 - 864)
	if tmp == ord(arkav[3]):
		print(n,v,p,tmp)
		mkilld[3] = [n,v,p]
# (mkilld[4].name.split("").sort().join("").charCodeAt(1) * 256 + (mkilld[4].proximity + mkilld[4].velocity + 30) * 82)
for n,v,p in zip(name, velocity, proximity):
	tmp = (ord(sorted(n)[1]) * 256 + (p + v + 30) * 82)
	if tmp == ord(arkav[4]):
		print(n,v,p,tmp)
		mkilld[4] = [n,v,p]
# ((mkilld[5].name.charCodeAt(4) + mkilld[5].proximity*8/5) * 100) 
for n,v,p in zip(name, velocity, proximity):
	tmp = ((ord(n[4%len(n)]) + p*8//5) * 100)
	if tmp == ord(arkav[5]):
		print(n,v,p,tmp)
		mkilld[5] = [n,v,p]

enc_flag = [149, 144, 62, 117, 233, 184, 141, 241, 230, 126, 250, 172, 56, 180, 137, 88, 159, 86, 132, 52, 208, 136, 76, 98, 186, 142, 151, 250, 153, 73, 48, 83, 184, 71, 245, 99, 135, 211, 3, 199, 70, 175, 204, 208, 105, 128, 167, 83, 114, 55, 102, 221, 80, 230, 82, 59, 137, 209, 196, 86, 13, 93, 170, 168, 48, 48, 99, 54, 90, 79, 236, 188, 136, 116, 216, 21, 1, 129, 55, 151, 201, 41, 19, 125, 119, 19, 248, 149, 210, 251, 166, 53, 118, 149, 168, 162, 168, 81, 136, 6, 79, 126, 97, 143, 44, 39, 20, 71, 105, 190, 47, 27, 158, 194, 169, 193, 37, 60, 146, 45, 184, 245, 125, 248, 212, 22, 75, 255, 212, 228, 23, 131, 75, 75, 140, 20, 148, 173, 189, 22, 226, 4, 26, 82, 0, 22, 115, 15, 254, 34, 203, 14, 178, 10, 122, 212, 77, 93, 32, 252, 109, 213, 117, 152, 70, 42, 182, 194, 82, 168, 164, 164, 16, 56, 29, 127, 142, 77, 172, 94, 142, 43, 138, 144, 136, 46, 161, 36, 241, 238, 163, 204, 225, 183, 28, 160, 255, 181, 113, 223, 198, 211, 89, 30, 63, 3, 91, 201, 6, 57, 135, 2, 183, 71, 113, 224, 205, 245, 175, 32, 221, 131, 216, 167, 89, 110, 96, 164, 196, 11, 194, 238, 88, 223, 163, 174, 205, 231, 121, 206, 163, 168, 100, 147, 181, 169, 67, 184, 245, 212, 86, 244, 79, 5, 220, 27, 40, 113, 193, 215, 94, 181, 239, 148, 166, 59, 172, 47, 211, 2, 94, 227, 255, 160, 167, 188, 212, 201, 135, 15, 239, 108, 24, 1, 213, 250, 163, 39, 84, 243, 237, 109, 126, 89, 240, 21, 72, 100, 127, 74, 117, 46, 151, 120, 245, 43, 124, 37, 178, 59, 28, 186, 46, 107, 165, 199, 195, 129, 240, 2, 250, 150, 148, 30, 18, 94, 195, 105, 158, 221, 134, 26, 196, 80, 23, 65, 172, 192, 253, 5, 126, 211, 64, 186, 103, 110, 1, 71, 234, 8, 44, 232, 57, 113, 65, 229, 108, 51, 159, 185, 36, 110, 80, 100, 52, 45, 79, 5, 65, 165, 195, 154, 158, 10, 19, 229, 30, 124, 75, 256, 222, 35, 47, 12, 226, 51, 224, 17, 162, 13, 225, 201, 173, 157, 12, 239, 250, 193, 0, 29, 224, 13, 220, 158, 100, 207, 61, 223, 3, 6, 164, 10, 159, 142, 11, 247, 164, 37, 107, 151, 188, 113, 203, 150, 154, 252, 28, 57, 150, 196, 113, 75, 19, 121, 9, 210, 135, 122, 198, 239, 71, 40, 170, 189, 198, 220, 28, 81, 141, 147, 3, 243, 122, 2, 167, 140, 128, 39, 88, 198, 27, 144, 25, 210, 256, 153, 56, 224, 77, 126, 122, 34, 172, 191, 60, 151, 100, 88, 249, 223, 254, 89, 202, 108, 189, 73, 255, 190, 105, 49, 247, 123, 27, 198, 33, 149, 167, 9, 162, 67, 107, 86, 3, 131, 252, 240, 91, 71, 128, 9, 106, 39, 237, 59, 187, 22, 115, 90, 255, 58, 200, 68, 134, 104, 138, 239, 23, 173, 54, 199, 49, 185, 244, 101, 169, 73, 218, 103, 79, 48, 124, 193, 107, 240, 133, 112, 233, 122, 45, 86, 31, 13, 133, 238, 81, 38, 188, 156, 55, 83, 197, 11, 192, 190, 39, 75, 71, 176, 8, 209, 7, 232, 137, 208, 250, 98]
for i in range(len(mkilld)):
    t1= hashlib.md5(mkilld[i][0].encode()).hexdigest()
    t2 = hashlib.md5(str(mkilld[i][1]).encode()).hexdigest();
    t3 = hashlib.md5(str(mkilld[i][2]).encode()).hexdigest();
    t4 = i*96;
    for j in range(32):
        enc_flag[t4+j] &= ord(t1[j])
        enc_flag[t4+j] += ord(t1[j])
    t4 += 32
    for j in range(32):
        enc_flag[t4+j] &= ord(t2[j])
        enc_flag[t4+j] += ord(t2[j])
    t4 += 32
    for j in range(32):
        enc_flag[t4+j] &= ord(t3[j])
        enc_flag[t4+j] += ord(t3[j])
tampung = []
for i in range(32):
    z = 0
    for j in range(len(mkilld)*3):
        z ^= enc_flag[i*len(mkilld)*3 + j]
    tampung.append(z)

enc_flag = [-88, -2, 2, 7, -26, -29, -11, -19, -152, -153, 48, 23, -172, -31, 49, 30, 32, 23, 11, -41, 34, 14, -73, -139, -174, 100, 61, -43, 78, 12, -136, -61]

for i in range(len(enc_flag)):
	tampung[i] += enc_flag[i]

flag = ''.join(chr(t) for t in tampung)
print("Arkav7{%s}" % flag)