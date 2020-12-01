
def swap_again(chr_inp):
	global setup_swap

	v2 - setup_swap[1]
	v3 = setup_swap[0]
	setup_swap[0] = v3
	v4 = setup_swap[v3 + 2]
	v5 = v4 + v2

	setup_swap[1] = v5
	setup_swap[v3 + 2] = setup_swap[v5 + 2]
	setup_swap[v5 + 2] = v4

	return chr_inp ^ setup_swap[setup_swap[v3 + v2] + 42]

def Setup_and_Swap(ret_arr, key, len_key):
	ret_arr = [i for i in range(256)]

	x = 0
	y = 0
	while (x !=  256):
		xx = x
		v7 = ret_arr[x]
		y += v7 + key[x % len_key]
		ret_arr[xx] = ret_arr[y%256]
		ret_arr[y%256] = v7
		x += 1
	return ret_arr


def loop_writeout(inp_file):
	global setup_swap
	out = []
	for chr_inp in inp_file:
		v20 = swap_again(setup_swap, chr_inp)
		out.append(v20)
		v21 = rand()
		out.append(v21)


ret_arr = []
key = 'v3ry_s3cur3_k3y'.encode()
setup_swap = Setup_and_Swap(ret_arr, key, len(key))
enc_flag =
for c in 
print(setup_swap)