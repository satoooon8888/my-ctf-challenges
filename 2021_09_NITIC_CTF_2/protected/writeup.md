# 表層解析

stringsコマンドを使ってバイナリ中にある文字列を見てみましょう。

```
$ strings chall
...
[]A\A]A^A_
PASSWORD:
sUp3r_s3Cr37_P4s5w0Rd
Invalid password.
:*3$"
GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
crtstuff.c
deregister_tm_clones
...
```

`sUp3r_s3Cr37_P4s5w0Rd`といういかにも怪しい文字列がありました。これがパスワードなので、入力すればフラグが得られます。

# 真面目に解析すると

Ghidraを使って解析してみます。

```c

/* WARNING: Could not reconcile some variable overlaps */

bool main(void)

{
  int result;
  long in_FS_OFFSET;
  char out [26];
  char input_buf [264];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  printf("PASSWORD: ");
  __isoc99_scanf("%s",input_buf);
  result = strcmp(input_buf,"sUp3r_s3Cr37_P4s5w0Rd");
  if (result == 0) {
    out._0_8_ = 0xe17e5dba42674ca9;
    out._8_8_ = 0x4027c7f0b9cb9dba;
    out._16_8_ = 0x30d97c7e02684487;
    out._24_2_ = 0x1d00;
    RC4(out,input_buf,0x1a);
    puts(out);
  }
  else {
    puts("Invalid password.");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return result != 0;
}
```

`sUp3r_s3Cr37_P4s5w0Rd`がパスワードで、それをkeyとしてRC4で暗号化されたフラグを復号していることがわかります。

