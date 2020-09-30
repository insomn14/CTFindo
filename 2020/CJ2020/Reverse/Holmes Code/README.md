<div style="text-align: justify">

# Holmes Code

### Deskripsi
```
This Code Secret Dr. Watson to Holmes, Please check message on the Code
```

Pada tantangan kali ini kita diberikan file *[code.zip](code.zip)* yang berisi file binary sejumlah *287* file. Berikut ini adalah sedikit potongan disassembly dari beberapa program binary tersebut.

```
┌──(unknow㉿unknow)-[~/…/CJ2020/Reverse/Holmes Code/code]
└─$ objdump -d -M intel code0
  ...
00000000006000b0 <.shellcode>:
  ...
  6000c2:       48 8b 44 24 10          mov    rax,QWORD PTR [rsp+0x10]
  6000c7:       8a 10                   mov    dl,BYTE PTR [rax]
  6000c9:       80 ea 1e                sub    dl,0x1e
  6000cc:       80 fa ec                cmp    dl,0xec
  ...

┌──(unknow㉿unknow)-[~/…/CJ2020/Reverse/Holmes Code/code]
└─$ objdump -d -M intel code1
  ...
00000000006000b0 <.shellcode>:
  ...
  6000c2:       48 8b 44 24 10          mov    rax,QWORD PTR [rsp+0x10]
  6000c7:       8a 10                   mov    dl,BYTE PTR [rax]
  6000c9:       80 ea 35                sub    dl,0x35
  6000cc:       80 fa 1f                cmp    dl,0x1f
  ...

┌──(unknow㉿unknow)-[~/…/CJ2020/Reverse/Holmes Code/code]
└─$ objdump -d -M intel code2
  ...
00000000006000b0 <.shellcode>:
  ...
  6000c2:       48 8b 44 24 10          mov    rax,QWORD PTR [rsp+0x10]
  6000c7:       8a 10                   mov    dl,BYTE PTR [rax]
  6000c9:       80 c2 19                add    dl,0x19
  6000cc:       80 fa 81                cmp    dl,0x81
  ...
```

Setelah diamati ternyata setiap binary memiliki alur kode program yang mmirip, namun masing-masing binary memiliki instruksi aritmatika yang berbeda-beda diantaranya *(add/sub/xor)*.

### Solusi

Langkah-langkah yang perlu dilakukan untuk menyelesaikan tantangan ini:
1. Membuat [bash script](solve.sh) untuk mengabil potongan kode dissassembly yang dibutuhkan.
```
┌──(unknow㉿unknow)-[~/…/CJ2020/Reverse/Holmes Code/code]
└─$ ./solve.sh > data.txt

┌──(unknow㉿unknow)-[~/…/CJ2020/Reverse/Holmes Code/code]
└─$ head data.txt
code0
  6000c9:       80 ea 1e                sub    dl,0x1e
  6000cc:       80 fa ec                cmp    dl,0xec
code1
  6000c9:       80 ea 35                sub    dl,0x35
  6000cc:       80 fa 1f                cmp    dl,0x1f
code2
  6000c9:       80 c2 19                add    dl,0x19
  6000cc:       80 fa 81                cmp    dl,0x81
code3
```
2. Membuat [python script](solver.py) untuk menyelesikan tantangan berdasarkan kode disassembly yang sudah kita dapatkan sebelumnya.
```
┌──(unknow㉿unknow)-[~/…/CJ2020/Reverse/Holmes Code/code]
└─$ python solver.py

The story is notable for introducing the character of Irene Adler, who is one of the most notable female characters in the Sherlock Holmes series, despite appearing in only one story.[1] Doyle ranked CJ2020{A_ScaNdal_in_B0h3mia} fifth in his list of his twelve favourite Holmes stories.
```

FLAG : `CJ2020{A_ScaNdal_in_B0h3mia}`

</div>