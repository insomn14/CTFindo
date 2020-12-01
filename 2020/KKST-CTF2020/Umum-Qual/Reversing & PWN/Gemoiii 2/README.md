# Solution 

## Encrypted Data :
```
~/K/Reversing & PWN/Gemoiii 2 ❯ xxd out
00000000: fc86 0950 79b4 d13d 249a a474 acc2 31fc  ...Py..=$..t..1.
00000010: 8ab5 7b29 26c7 e25e 51e8 972b c7f1 4800  ..{)&..^Q..+..H.
00000020: 33c6 5097 f489 53b0 71b9 d9d5 dac8 764a  3.P...S.q.....vJ
00000030: 6920 fd3d 4cf8 21c1 8feb 1a8d 2c32 74d5  i .=L.!.....,2t.
00000040: 62a8 6daf ed06 e1e7 b101 6431 2e1e e90f  b.m.......d1....
00000050: 4d85 7af5 a71d ea69 bcab e32a 7ecd 5aaf  M.z....i...*~.Z.
```

- `00000000` 16 bytes pertama adalah nilai dari `rand()` yang ditulis oleh fungsi `fwrite()`.
- `00000010` 16 bytes berikutnya adalah tempat key disimpan setelah dixor dengan nilai `rand()` lalu ditulis dengan fungsi `fputs()`.

## Recovery Key :
```
>>> from pwn import xor
>>> rand = bytes.fromhex('fc86095079b4d13d249aa474acc231fc')
>>> sec2 = bytes.fromhex('8ab57b2926c7e25e51e8972bc7f14800')
>>> xor(rand,sec2)
b'v3ry_s3cur3_k3y\xfc'
```

## Dump Encrypted Flag:
- Selama proses enkripsi berlangsung setiap karakter pada flag akan dixor dengan nilai acak.
- Setiap karakter hasil xor akan pisah dengan nilai `rand()`.
- Skip setiap 1 byte yang ada pada `out` file untuk mendapatkan flag yang telah terenkripsi.
```
>>> f = open('out', 'rb').read()
>>> enc_flag = [f[32:][i] for i in range(0, len(f[32:]), 2)]
>>>
>>> len(enc_flag)
32
>>> print(*[hex(i)[2:] for i in enc_flag])
	33 50 f4 53 71 d9 da 76 69 fd 4c 21 8f 1a 2c 74 62 6d ed e1 b1 64 2e e9 4d 7a a7 ea bc e3 7e 5a
```

```
~/K/Reversing & PWN/Gemoiii 2 ❯ echo -ne '\x33\x50\xf4\x53\x71\xd9\xda\x76\x69\xfd\x4c\x21\x8f\x1a\x2c\x74\x62\x6d\xed\xe1\xb1\x64\x2e\xe9\x4d\x7a\xa7\xea\xbc\xe3\x7e\x5a' > enc_flag.txt
```

## Debugging :
1. Masukan Parameter sebagain berikut:
```
encrypt v3ry_s3cur3_k3y enc_flag.txt outfile
```
2. Set breakpoint pada alamat `0000000000402DD1` dan tekan `<F9>`.
3. Setelah hit breakpoint ubah 16 bytes pada `[rbx-1]` dengan 16 bytes `rand()` pada file `out` sebelumnya.
4.  Kemudian tekan `<F9>` untuk menjalankan process debugging sampai selesai. 

## Hasil Output File Debugging:
```
~/K/R/Gemoiii 2 ❯ xxd outfile                                     took 6m 46s
00000000: fc86 0950 79b4 d13d 249a a474 acc2 31fc  ...Py..=$..t..1.
00000010: 8ab5 7b29 26c7 e25e 51e8 972b c7f1 4800  ..{)&..^Q..+..H.
00000020: 4ba9 4b7b 53e6 5477 32fb 30b7 32db 30d8  K.K{S.Tw2.0.2.0.
00000030: 7b56 776a 33ba 6c94 6358 3005 6d3c 3351  {Vwj3.l.cX0.m<3Q
00000040: 5f98 741a 30bf 5fc2 7295 6379 34e1 6ee0  _.t.0._.r.cy4.n.
00000050: 73ed 3099 6d4e 7777 34d0 7239 33d6 7de5  s.0.mNww4.r93.}.
```
## Extract Flag:
```
>>> get = open('outfile', 'rb').read()
>>>
>>> val = [get[32:][i] for i in range(0, len(get[32:]), 2)]
>>> ''.join(chr(i) for i in val)
'KKST2020{w3lc0m3_t0_rc4ns0mw4r3}'
```
