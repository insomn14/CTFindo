<div style="text-align: justify">

# Home Sherlock

### Deskripsi
```
Number Home Sherlock Holmes ?

Please check on the File

Download home : https://drive.google.com/file/d/14P7xZ4XIsEm6HU5WMvOVw6E0BFRH6CuH/view
```

Di tantangan kali ini kita diberikan file binary dari golang [*home*](home). Berikut ini adalah pseudocode dari binary tersebut.

```
[0x00454ed0]> pdg@sym.main.main

void sym.main.main(int64_t arg1, int64_t arg2)
{
...
auStack24 = CONCAT88(0x4e9270, 0x4ab9c0);
    sym.fmt.Fprintln(arg1, arg2, (int64_t)obj.go.itab._os.File_io.Writer);
    sym.runtime.newobject();
    auStack40 = CONCAT88(placeholder_3, 0x4a5ca0);
    sym.fmt.Fscanln();
    if (*placeholder_3 == 0x9dbdf7f4c117ec) {
        sym.runtime.convTstring(arg1, arg2, arg3, placeholder_3, in_R8, in_R9);
        sym.fmt.Fprintln(arg1, arg2, arg3_00);
    } else {
        sym.fmt.Fprintln(arg1, arg2, arg3);
    }
    sym.fmt.Fscanln();
...
```
Jika file binary tersebut di eksekusi maka program akan meminta inputan, jika di perhatikan setelah pemanggilan fungsi `sym.fmt.Fscanln();` terdapat perbandingan perintah `if` yang membandingkan pointer *"\*placeholder_3"* dengan nilai hexadesimal *"0x9dbdf7f4c117ec"*.

```

[0x00454ed0]> pdf@sym.main.main
            ; CODE XREF from sym.main.main @ 0x4997a0
            ;-- sym.go.main.main:
┌ 597: sym.main.main (int64_t arg1, int64_t arg2);
...
...
│      │╎   0x00499643      48c744242001.  mov qword [var_20h], 1
│      │╎   0x0049964c      e8afa2ffff     call sym.fmt.Fscanln
│      │╎   0x00499651      48b8ec17c1f4.  movabs rax, 0x9dbdf7f4c117ec
│      │╎   0x0049965b      488b4c2440     mov rcx, qword [var_40h]
│      │╎   0x00499660      483901         cmp qword [rcx], rax
│     ┌───< 0x00499663      0f85d5000000   jne 0x49973e
│     ││╎   0x00499669      488d052bb803.  lea rax, [0x004d4e9b]       ; "Q0oyMDIwezIyMUJfQmFrZXJfU3RyMzN0fQofile type does not support deadlinefindfunc: bad findfunctab entry idxfindrunnable: netpoll "
│     ││╎   0x00499670      48890424       mov qword [rsp], rax
│     ││╎   0x00499674      48c744240823.  mov qword [var_8h], 0x23    ; '#'
...

[0x00454ed0]> ps 35 @ 0x004d4e9b
Q0oyMDIwezIyMUJfQmFrZXJfU3RyMzN0fQo
```
Pada saat kami melihat fungsi main dengan tampilan kode disassembly pada radare2, kita dapat melihat dengan jelas terdapat sebuah string yang aneh.

### Solution

Dari informasi yang sudah kita dapat sebelumnya selama melakukan static analysis, terdapat dua cara untuk menyelesaikan tantangan ini.

1. Decode *"Q0oyMDIwezIyMUJfQmFrZXJfU3RyMzN0fQo"* kedalam base64.
```
┌──(unknow㉿unknow)-[~/…/2020/CJ2020/Reverse/Home Sherlock]
└─$ echo 'Q0oyMDIwezIyMUJfQmFrZXJfU3RyMzN0fQo' | base64 -d
CJ2020{221B_Baker_Str33t}
base64: invalid input
```

2. Ubah nilai hexadesimal *"0x9dbdf7f4c117ec"* kedalam desimal lalu jadikan sebagai inputan.
```
┌──(unknow㉿unknow)-[~/…/2020/CJ2020/Reverse/Home Sherlock]
└─$ python -c 'print(0x9dbdf7f4c117ec)'
44400444004440044

┌──(unknow㉿unknow)-[~/…/2020/CJ2020/Reverse/Home Sherlock]
└─$ ./home 
Sherlock Holmes Home
44400444004440044
Q0oyMDIwezIyMUJfQmFrZXJfU3RyMzN0fQo

┌──(unknow㉿unknow)-[~/…/2020/CJ2020/Reverse/Home Sherlock]
└─$ echo 'Q0oyMDIwezIyMUJfQmFrZXJfU3RyMzN0fQo' | base64 -d
CJ2020{221B_Baker_Str33t}
base64: invalid input
```

FLAG : `CJ2020{221B_Baker_Str33t}`

</div>