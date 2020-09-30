<div style="text-align: justify">

# Pawon

### Deskripsi
```
Yet another reverse engineering challenge
```

Pada tantangan berikut ini kita diberikan file binary *[pawon](pawon)*, dan berikut ini adalah potongan pseudocode kode dari fungsi `main` program tersebut yang sudah saya modif sedikit.

```
...
    sym.banner();
    sym.imp.printf(" Enter Your Mail\n > ");
    sym.imp.std::basic_istream_char__std::(reloc.std::cin, &s);

    sym.imp.printf(" Enter Serial\n > ");
    sym.imp.std::basic_istream_char__std::(reloc.std::cin);

    var_18h._0_4_ = 0;
    while( true ) {
        uVar7 = SEXT48((int32_t)var_18h);
        uVar3 = sym.imp.strlen(&s);
        if (uVar3 <= uVar7) break;
        if (*(char *)((int64_t)&s + (int64_t)(int32_t)var_18h) == '@') {
            var_18h._7_1_ = '\x01';
        }
        var_18h._0_4_ = (int32_t)var_18h + 1;
    }
    if (var_18h._7_1_ == '\x01') {
        uVar3 = sym.imp.strlen(&s);
        if (3 < uVar3) goto code_r0x0000138d;
    }
    sym.seret();
...
```

Ketika saat mengeksekusi program tersebut kita akan diminta untuk memasukan dua inputan, yaitu *Mail* dan *Serial*. Terdapa pengecekan *Mail* yang mana inputan kita harus memiliki karakter *"@"* dan panjangnya harus lebih dari 3.

```
...
code_r0x0000138d:
    uVar3 = sym.imp.strlen();
    if (uVar3 < 0x19) {
        sym.seret();
    }
    if (((var_430h._5_1_ != '-') && (var_425h != '-')) && (var_41eh != '-')) {
        sym.seret();
    }
    if ((char)var_430h != var_426h) {
        sym.seret();
    }
    if (var_430h._1_1_ != 'e') {
        sym.seret();
    }
    if (var_430h._3_1_ != 'P') {
        sym.seret();
    }
    if ((char)var_417h != '\0') {
        sym.seret();
    }
    if (var_430h._2_1_ != 'm') {
        sym.seret();
    }
    if (var_430h._4_1_ != var_430h._1_1_) {
        sym.seret();
    }
    if (var_430h._6_1_ != 'j') {
        sym.seret();
    }
    if (var_430h._7_1_ != 'o') {
        sym.seret();
    }
    if (var_428h != var_427h) {
        sym.seret();
    }
    if (var_427h != 'S') {
        sym.seret();
    }
    cVar2 = sym.check_char__char__int
                      ((uint64_t)(uint32_t)(int32_t)var_430h._5_1_, (uint64_t)(uint32_t)(int32_t)var_424h, 9);
    if (cVar2 != '\x01') {
        sym.seret();
    }
    if ((int32_t)var_419h != var_41fh + 3) {
        sym.seret();
    }
    if (var_423h != var_41ch) {
        sym.seret();
    }
    if (var_422h != 'z') {
        sym.seret();
    }
    cVar2 = sym.check_char__char__int
                      ((uint64_t)(uint32_t)(int32_t)var_421h, (uint64_t)(uint32_t)(int32_t)var_420h, 0xffffff7a);
    if (cVar2 != '\x01') {
        sym.seret();
    }
    if (var_41bh != 'T') {
        sym.seret();
    }
    if (var_420h != 'H') {
        sym.seret();
    }
    if (var_41ch != 'u') {
        sym.seret();
    }
    if (var_41fh != '5') {
        sym.seret();
    }
    if (var_41dh != 'S') {
        sym.seret();
    }
    if (var_41ah != '1') {
        sym.seret();
    }
    if (var_426h != var_41bh) {
        sym.seret();
    }
    cVar2 = sym.check_char__char__int
                      ((uint64_t)(uint32_t)(int32_t)var_418h, (uint64_t)(uint32_t)(int32_t)var_41ch, 0xffffffc3);
    if (cVar2 != '\x01') {
        sym.seret();
    }
```

Bagian ini adalah pengecekan dari inputan *Serial*.

### Solusi

Sama seperti tantangan *BabyBaby* yang sebelumnya, untuk menyelesaikan tantangan ini kita dapat menggunakan library python z3-solver.

[solver.py](solver.py)

```
┌──(unknow㉿unknow)-[~/…/2020/CJ2020/Reverse/Pawon]
└─$ python solver.py
TemPe-joSST-cuzgH5-SuT18­Y
                                                                           
┌──(unknow㉿unknow)-[~/…/2020/CJ2020/Reverse/Pawon]
└─$ ./pawon
          -------                
          CJ 2020                
          -------                
 Enter Your Mail
 > test@mail.com
 Enter Serial
 > TemPe-joSST-cuzgH5-SuT18Y

  CJ2020{r+jKctQn&m14l,.JBH8WckZj}
```

FLAG : `CJ2020{r+jKctQn&m14l,.JBH8WckZj}`

</div>