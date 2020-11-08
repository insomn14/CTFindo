

float __fastcall bagi(float a1, float a2)
{
  return a1 / a2;
}

__int64 __fastcall kurang(int a1, int a2)
{
  return (unsigned int)(a1 - a2);
}


__int64 __fastcall jumlah(int a1, int a2)
{
  return (unsigned int)(a1 + a2);
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // eax
  double v4; // xmm0_8
  __m128i v5; // xmm2
  int result; // eax
  char v7[32]; // [rsp+0h] [rbp-40h]
  int v8; // [rsp+20h] [rbp-20h]
  __int16 v9; // [rsp+26h] [rbp-1Ah]
  int v10; // [rsp+28h] [rbp-18h]
  unsigned int v11; // [rsp+2Ch] [rbp-14h]
  unsigned int v12; // [rsp+30h] [rbp-10h]
  int j; // [rsp+34h] [rbp-Ch]
  int i; // [rsp+38h] [rbp-8h]
  int v15; // [rsp+3Ch] [rbp-4h]

  v3 = time(0LL);
  srand(v3);
  v12 = rand() % 100 + 1;
  v11 = rand() % 100 + 1;
  puts("Kumpulan Soal Latihan Matematika");
  puts("1. Penjumlahan");
  puts("2. Pengurangan");
  puts("3. Perkalian");
  puts("4. Pembagian");
  puts("0. Keluar");
  puts("Pilih salah satu menu");
  __isoc99_scanf("%d", &v9);
  switch ( v9 )
  {
    case 0:
      exit(0);
      return result;
    case 1:
      puts("Anda memilih penjumlahan");
      v10 = jumlah(v12, v11);
      printf("%d + %d = ", v12, v11);
      __isoc99_scanf("%d", &v8);
      if ( v10 == v8 )
        goto LABEL_3;
      goto LABEL_6;
    case 2:
      puts("Anda memilih pengurangan");
      v10 = kurang(v12, v11);
      printf("%d - %d = ", v12, v11);
      __isoc99_scanf("%d", &v8);
      if ( v10 == v8 )
LABEL_3:
        printf("jawaban benar");
      else
LABEL_6:
        printf("jawaban salah");
      return 0;
    case 3:
      if ( v9 != 3 )
      {
        puts("Program akan keluar");
        exit(0);
      }
      puts("Latihan hanya bisa penjumlahan dan pengurangan");
      puts("Jika punya kode masukkan");
      __isoc99_scanf("%s", v7);
      for ( i = 0; i <= 15; ++i )
      {
        if ( (v7[i] ^ iii[i]) == jjj[i] )
          ++v15;
      }
      if ( v15 != 16 )
        goto LABEL_17;
      puts("berhasil");
      puts("Anda memilih perkalian");
      v10 = (int)(double)(int)kali(v12, v11);
      printf("%d * %d = ", v12, v11);
      __isoc99_scanf("%d", &v8);
      if ( v10 == v8 )
        goto LABEL_15;
      printf("jawaban salah");
      break;
    case 4:
      if ( v9 != 4 )
      {
        puts("Program akan keluar");
        exit(0);
      }
      puts("Latihan hanya bisa penjumlahan dan pengurangan");
      puts("Jika punya kode masukkan");
      __isoc99_scanf("%s", v7);
      for ( j = 0; j <= 25; ++j )
      {
        if ( (v7[j] ^ ii[j]) == jj[j] )
          ++v15;
      }
      if ( v15 == 26 )
      {
        puts("berhasil");
        puts("Anda memilih pembagian");
        HIDWORD(v4) = 0;
        *(float *)&v4 = (float)(int)v11;
        v5 = 0LL;
        *(float *)v5.m128i_i32 = (float)(int)v12;
        v10 = (int)bagi(*(double *)_mm_cvtsi32_si128(_mm_cvtsi128_si32(v5)).m128i_i64, v4);
        printf("%d / %d = ", v12, v11);
        __isoc99_scanf("%d", &v8);
        if ( v10 == v8 )
LABEL_15:
          printf("jawaban benar");
        else
          printf("jawabansalah");
      }
      else
      {
LABEL_17:
        puts("salah");
      }
      break;
    default:
      puts("Pilihan diluar ketentuan");
      exit(0);
      return result;
  }
  return 0;
}