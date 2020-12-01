def sstt(x):
  6           0 LOAD_FAST                0 (x)
              2 LOAD_CONST               0 (None)
              4 LOAD_CONST               0 (None)
              6 LOAD_CONST               1 (-1)
              8 BUILD_SLICE              3
             10 BINARY_SUBSCR
             12 STORE_FAST               0 (x)

  7          14 LOAD_CONST               2 ('')
             16 STORE_FAST               1 (t)

  8          18 LOAD_GLOBAL              0 (random)
             20 LOAD_METHOD              1 (randint)
             22 LOAD_CONST               3 (1)
             24 LOAD_CONST               4 (6000)
             26 CALL_METHOD              2
             28 STORE_FAST               2 (k)

  9          30 LOAD_GLOBAL              0 (random)
             32 LOAD_METHOD              1 (randint)
             34 LOAD_CONST               5 (0)
             36 LOAD_CONST               4 (6000)
             38 CALL_METHOD              2
             40 STORE_FAST               3 (s)

 10          42 LOAD_FAST                0 (x)
             44 GET_ITER
        >>   46 FOR_ITER                28 (to 76)
             48 STORE_FAST               4 (c)

 12          50 LOAD_FAST                1 (t)
             52 LOAD_GLOBAL              2 (chr)
             54 LOAD_GLOBAL              3 (ord)
             56 LOAD_FAST                4 (c)
             58 CALL_FUNCTION            1
             60 LOAD_FAST                2 (k)
             62 BINARY_SUBTRACT
             64 LOAD_FAST                3 (s)
             66 BINARY_XOR
             68 CALL_FUNCTION            1
             70 INPLACE_ADD
             72 STORE_FAST               1 (t)
             74 JUMP_ABSOLUTE           46

 14     >>   76 LOAD_GLOBAL              4 (b64encode)
             78 LOAD_FAST                1 (t)
             80 LOAD_METHOD              5 (encode)
             82 LOAD_CONST               6 ('utf-8')
             84 CALL_METHOD              1
             86 CALL_FUNCTION            1
             88 RETURN_VALUE



flag = "flag_lupa_to_delete_ayo_cepat_submit_!"
crypt_flag = sstt(flag)
print(crypt_flag)