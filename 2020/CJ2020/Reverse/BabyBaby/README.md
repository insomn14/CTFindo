<div style="text-align: justify">

# BabyBaby

### Description
```
Binary ini dapat digunakan untuk permulaan belajar reverse engineering.

Tips: Soal ini lebih mudah dikerjakan dengan static analysis seperti menggunakan Ghidra (gratis) atau IDA Pro (berbayar) dengan meng-generate kode C-like dari kode mesin yang ada di dalam binary.
```

### Problem
Pada tantangan ini kita diberikan file binary *[BabyBaby](BabyBaby)*, dan berikut ini adalah pseudocode dari fungsi main program tersebut.

```
    sym.imp.printf(0x9e4);                                      //  ps @ 0x9e4 = "Masukkan 3 angka:"
    sym.imp.__isoc99_scanf(0x9f7, &c, &var_14h);                //  ps @ 0x9f7 = "%d %d %d"
    if (((c + var_14h == (uint32_t)var_10h * c) &&
        ((int32_t)var_14h / (int32_t)(uint32_t)var_10h == 0x14)) &&
        ((int32_t)var_14h / (int32_t)c == 3)) {
        var_10h._4_4_ = 0;
        sym.imp.puts(0xa00, c, (int32_t)var_14h % (int32_t)c);  //  ps @ 0xa00 = "Benar!"
        var_10h._4_4_ = 0;
        while (var_10h._4_4_ < 0x15) {
            if (var_10h._4_4_ % 3 == 0) {
                sym.imp.putchar(c ^ *(uint32_t *)("X" + (int64_t)var_10h._4_4_ * 4));
            }
            if (var_10h._4_4_ % 3 == 1) {
                sym.imp.putchar(var_14h ^ *(uint32_t *)("X" + (int64_t)var_10h._4_4_ * 4));
            }
            if (var_10h._4_4_ % 3 == 2) {
                sym.imp.putchar((uint32_t)var_10h ^ *(uint32_t *)("X" + (int64_t)var_10h._4_4_ * 4));
            }
            var_10h._4_4_ = var_10h._4_4_ + 1;
        }
    } else {
        sym.imp.puts(0xa07);        //  ps @ 0xa07 = "Salah!" 
    }
```
*Pengecekan kondisi :*
```
if ((first + third == second * first)
&& (third / second == 0x14)
&& (third / first == 3))
```

Seperti yang kita lihat `scanf` menerima 3 masukan sebagai integer, masing-masing masukan akan dihitung dalam kondisi `if`. jika hasilnya `true` maka
program akan mencetak string *"Benar"* dan juga *Flag*.

### Solution
Untuk menyelesaikan tantangan ini kita dapat menggunakan library python z3-solver.

```
>>> from z3 import *
>>> 
>>> inp = [BitVec(f'input_{i}',8)for i in range(1,4)]
>>> 
>>> s = Solver()
>>> s.add(inp[0] + inp[1] == inp[0] * inp[2], inp[1] / inp[2] == 20, inp[1] / inp[0] == 3)
>>> s.check()
sat
>>> s.model()
[input_2 = 81, input_3 = 4, input_1 = 27]
``` 
```
┌──(unknow㉿unknow)-[~/…/2020/CJ2020/Reverse/BabyBaby]
└─$ ./BabyBaby 
Masukkan 3 angka: 27 81 4
Benar!
CJ2020{b4A4a4BBbb7yy}
```

FLAG : `CJ2020{b4A4a4BBbb7yy}`

</div>
