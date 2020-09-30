<div style="text-align: justify">

# Ransomnware

### Deskripsi

```
Reverse engineering berguna untuk mengetahui alur dari suatu program baik untuk riset binary exploitation, membuat crack/patch, membuat keygen, ataupun analisis malware.

Berikut adalah sebuah ransomware yang mengenkripsi berkas flag.txt. Dapatkah Anda mendekripsi berkas tersebut?
```

Pada tantangan ini kita diberikan file binary [*ransomnware*](ransomnware) dan juga sebuah file [*flag*](flag.txt.enc) yang telah terenkripsi. Berikut ini adalah potongan-potongan pseudocode dari file binary tersebut.

**Catatan : beberapa nama fungsi dan variabel telah kami ubah agar lebih mudah dibaca.*


```
[0x000006e0]> pdg @ randomVal
void randomVal(int64_t arg1)
{
    ...    
    canary = *(int64_t *)(in_FS_OFFSET + 0x28);
    fildes._0_4_ = sym.imp.open(0xcd5, 0);      // /dev/urandom
    sym.imp.read((undefined4)fildes, (int64_t)&fildes + 4, 0x20, (int64_t)&fildes + 4);
    sym.imp.close((undefined4)fildes);
    *(int64_t *)arg1 = stack0xffffffffffffffc8;
    *(void **)(arg1 + 8) = var_28h;
    *(int64_t *)(arg1 + 0x10) = Flag;
    *(int64_t *)(arg1 + 0x18) = var_18h;
    ...
}
```
```
[0x000006e0]> pdg @ fillArr
undefined8 fillArr(void)
{
    undefined8 I;
    
    I = 0;
    while (I < 0x100) {
        *(FillArray + I) = I;
        I = I + 1;
    }
    *VAR_1 = 0;
    *VAR_2 = 0;
    return 1;
}
```
```
[0x000006e0]> pdg @ swapVal
void swapVal(int64_t arg1, int64_t arg2)
{
    ...    
    uVar1 = *(undefined *)arg1;
    *(undefined *)arg1 = *(undefined *)arg2;
    *(undefined *)arg2 = uVar1;
    return;
}
```
```
[0x000006e0]> pdg @ procSwap
void procSwap(int64_t arg1, int64_t arg2)
{
    ...
    *VAR_2 = 0;
    while (*VAR_2 < 0x100) {
        iVar2 = *(FillArray + VAR_2) + *VAR_1 + *(arg1 + *VAR_2 % arg2);
        uVar1 = (iVar2 >> 0x1f) >> 0x18;
        *VAR_1 = (iVar2 + uVar1 & 0xff) - uVar1;
        swapVal(*(FillArray + VAR_2), *(FillArray + *VAR_1));
        *VAR_2 = *VAR_2 + 1;
    }
    *VAR_1 = 0;
    *VAR_2 = 0;
    return;
}
```
```
[0x000006e0]> pdg @ main
undefined8 main(undefined8 argc, char **argv)
{
    ...
    canary = *(int64_t *)(in_FS_OFFSET + 0x28);
    Flag._0_4_ = 1;
    Flag._4_4_ = sym.imp.open("flag.txt", 0);
    if (Flag._4_4_ == -1) {
    // WARNING: Subroutine does not return
        sym.imp.exit(0xffffffff);
    }
    FlagEnc = sym.imp.open("flag.txt.enc", 0x41);
    if (FlagEnc == 0xffffffff) {
    // WARNING: Subroutine does not return
        sym.imp.exit(0xffffffff);
    }

    randomVal(RandArr);
    var_14h = 0x20;
    fillArr();
    procSwap(*0x202010, 0x10); // 0x202010 -> "rhcmem__c\xadem__\xdaC"
    ...
```

Setelah binary mengload file `flag.txt` dan `flag.txt.enc`, program memanggil fungsi `randomVal(RandArr);` yang mana variabel `RandArr` akan menyimpan nilai random sepanjang 32 byte dari `/dev/urandom`.

Berikutnya fungsi `fillArr();` akan membuat sebuah array yang memiliki nilai 0 s/d 255 dan disimpan pada `FillArray`. 

Selanjutnya terdapat pemanggilan fungsi `procSwap(0x202010,16)`, pada fungsi ini setiap index dari `FillArray` akan calculated 32 byte dari `0x202010`, lalu dengan `swapVal` setiap indeks pada `FillArray` posisinya akan ditukar. 

```
[0x000006e0]> pdg @ getValFromArr
undefined getValFromArr(void)
{
    uint32_t uVar1;
    
    uVar1 = (*VAR_2 + 1 >> 0x1f) >> 0x18;
    *VAR_2 = (*VAR_2 + 1 + uVar1 & 0xff) - uVar1;
    *VAR_1 = *(FillArray + VAR_2) + *VAR_1;
    uVar1 = (*VAR_1 >> 0x1f) >> 0x18;
    *VAR_1 = (*VAR_1 + uVar1 & 0xff) - uVar1;
    swapVal(*(FillArray + VAR_2), *(FillArray + VAR_1));
    return *(FillArray (*(FillArray + VAR_1) + *(FillArray + VAR_2)));
}
```
```
    ...
    var_14h = 16;
    ...
    J = 0;
    while (J < (int32_t)var_14h) {
        var_25h = getValFromArr();
        ptr = *(RandArr + J) ^ var_25h;
        sym.imp.write(FlagEnc, &ptr, 1);
        J = J + 1;
    }
    fillArr();
    procSwap(RandArr, var_14h);
    while( true ) {
        Flag._0_4_ = sym.imp.read(Flag._4_4_, &buf, 1, &buf);
        if ((int32_t)Flag < 1) break;
        var_25h = getValFromArr();
        ptr = buf ^ var_25h;
        sym.imp.write(FlagEnc, &ptr, 1, &ptr);
    }
    sym.imp.close(Flag._4_4_);
    sym.imp.close(FlagEnc);
    ...
```



Pada bagian ini terdapat looping sebanyak 16x, dimana setiap indeks yang ada pada `RandArr` akan di XOR dengan nilai yang didapat dari fungsi `getValFromArr();`. Setiap nilai yang ada pada indeks `FillArray` akan swap, setiap kali terjadi pemanggilan pada fungsi `getValFromArr();`. Setiap hasil XOR antara `RandArr` dan `var_25h` akan ditulis pada `FlagEnc`.

Selanjutnya terdapat pemanggialn fungsi `fillArr();` dan `procSwap(RandArr,var_14h);`, kurang lebih penjelasnya hampir sama dengan yang sebelumnya. Namun kali ini variabel setiap indeks `FillArray` akan di calculated dengan 32 byte dari `RandArr`, kemudian setiap indeksnya akan swap dengan fungsi `swapVal`.

Berikutnya terdapat looping dimana `buf` akan menyimpan setiap 1byte dari `Flag._4_4_`. Kemudian `buf` di XOR dengan `var_25h` yang nilainya didapat dari `getValFromArr();`, hasil calculated `buf` dan `var_25h` akan ditulis pada `FlagEnc`.

### Solusi

Cara untuk mendekripsi :

1. Membuat array[256].
2. Melakukan perhitungan setiap indeks pada array[256] dengan `0x202010`.
3. Swap setiap posisi yang ada pada array[256].
4. Mengambil nilai dari array[256], lalu array[256] di swap kembali.
5. Melakukan xoring terhadap 32 byte pertama dari [*flag*](flag.txt.enc) dengan nilai yang telah dapat dari array[256].
   
   **Catatan: kita telah berhasil mengembalikan nilai 32 byte dari  `/dev/random`*
6. Ulangi kembali langkah 1 s/d 4. Namun pada langkah kedua array[256] akan di perhitungkan dengan `/dev/urandom` yang telah kita dapatkan sebelumnya.
7. Melakukan xoring terhadap sisa dari 32 byte pertama pada [*flag*](flag.txt.enc) dengan nilai yang kita dapat dari array[256].
   
   **Catatan: selamat kita telah berhasil mengembalikan [*flag*](flag.txt.enc) seperti semula*

Berikut ini adalah PoC dari [solver](solver.py) saya.
```
┌──(unknow㉿unknow)-[~/…/2020/CJ2020/Reverse/Ransomnware]
└─$ python solver.py 
CJ2020{mamntap_gan_c71c416369bb6230}

```

FLAG : `CJ2020{mamntap_gan_c71c416369bb6230}`

</div>