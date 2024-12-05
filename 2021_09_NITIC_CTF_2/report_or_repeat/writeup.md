# 解析

Ghidraで解析します。entryを見るとmain関数は`FUN_001014bd`であることがわかるので見ていきましょう。

```c

int main(int argc,char **argv)

{
  int read_len2;
  FILE *input_fp;
  FILE *output_fp;
  size_t read_len;
  ulong path_len;
  char *pcVar1;
  long in_FS_OFFSET;
  byte const_zero;
  int i;
  undefined input_buf [256];
  undefined output_buf [255];
  undefined4 output_path;
  undefined auStack277 [261];
  long canary;
  char path_i;
  
  const_zero = 0;
  canary = *(long *)(in_FS_OFFSET + 0x28);
  if (argc < 2) {
    printf("Usage: %s ./file\n",*argv);
    read_len2 = 0;
  }
  else {
    input_fp = fopen(argv[1],"rb");
    if (input_fp == (FILE *)0x0) {
      printf("Could not open %s\n",argv[1]);
      read_len2 = 1;
    }
    else {
      strncpy((char *)((long)&output_path + 1),argv[1],0x100);
      path_len = 0xffffffffffffffff;
      pcVar1 = (char *)((long)&output_path + 1);
      do {
        if (path_len == 0) break;
        path_len = path_len - 1;
        path_i = *pcVar1;
        pcVar1 = pcVar1 + (ulong)const_zero * -2 + 1;
      } while (path_i != '\0');
                    /* .enc */
      *(undefined4 *)((long)&output_path + ~path_len) = 0x636e652e;
      auStack277[~path_len] = 0;
      output_fp = fopen((char *)((long)&output_path + 1),"wb");
      if (output_fp == (FILE *)0x0) {
        printf("Could not open %s\n",(long)&output_path + 1);
        read_len2 = 1;
      }
      else {
        do {
          read_len = fread(input_buf,1,0x100,input_fp);
          read_len2 = (int)read_len;
          if (read_len2 < 0x100) {
            i = read_len2;
            if (read_len2 == 0) break;
            for (; i < 0x100; i = i + 1) {
              input_buf[i] = 0;
            }
          }
          encrypt(input_buf,output_buf);
          read_len = fwrite(output_buf,1,0x100,output_fp);
          if (read_len < 0x100) {
            printf("Failed to write to %s\n",(long)&output_path + 1);
            read_len2 = 1;
            goto LAB_00101738;
          }
        } while (read_len2 == 0x100);
        fclose(input_fp);
        fclose(output_fp);
        read_len2 = 0;
      }
    }
  }
LAB_00101738:
  if (canary == *(long *)(in_FS_OFFSET + 0x28)) {
    return read_len2;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}
```

解析するとこんな感じで、`argv[1]`のファイルを0x100バイト読み込み暗号化をしてから`{argv[1]}.enc`のファイルに書き込んでいます。encrypt関数について見ていきましょう。

```c

/* WARNING: Could not reconcile some variable overlaps */

void encrypt(byte *input_buf,byte *output_buf)

{
  long lVar1;
  long in_FS_OFFSET;
  int i;
  char xor_table [256];
  
  lVar1 = *(long *)(in_FS_OFFSET + 0x28);
  xor_table._0_8_ = 0xc2b5e93852ec1e72;
  xor_table._8_8_ = 0x27ea0f531f754746;
  xor_table._16_8_ = 0x2a898c8c6ed757cf;
  xor_table._24_8_ = 0x12e7a197b8a86f2;
  xor_table._32_8_ = 0x7c9f5b2bd30815ab;
  xor_table._40_8_ = 0x58826f3c985dde86;
  xor_table._48_8_ = 0x9ef377a56285eaf2;
  xor_table._56_8_ = 0x1b71a09e8b10373e;
  xor_table._64_8_ = 0x650117b32f7e9dce;
  xor_table._72_8_ = 0xf928e1ad2f795c14;
  xor_table._80_8_ = 0xa65e121f693a9255;
  xor_table._88_8_ = 0x28e33b47dadba441;
  xor_table._96_8_ = 0x627c22fa9ce90908;
  xor_table._104_8_ = 0x8e45e495862805d2;
  xor_table._112_8_ = 0x426458ed66ebe7d2;
  xor_table._120_8_ = 0x685191a02170a9ba;
  xor_table._128_8_ = 0x7abb33126ca97eff;
  xor_table._136_8_ = 0x1047cceede01bde;
  xor_table._144_8_ = 0xd3061b78361723cf;
  xor_table._152_8_ = 0xd4a5086985e255e;
  xor_table._160_8_ = 0xc22b726e96390c31;
  xor_table._168_8_ = 0xf9a944d74cdd310f;
  xor_table._176_8_ = 0xb0a67368b940edb7;
  xor_table._184_8_ = 0x4ce4b603372e3eef;
  xor_table._192_8_ = 0x6254f01074835dcb;
  xor_table._200_8_ = 0x846ea7ff5cdf28c1;
  xor_table._208_8_ = 0x3d175ba063eb3959;
  xor_table._216_8_ = 0x98777b218bcbee97;
  xor_table._224_8_ = 0x670388d4459a9d5;
  xor_table._232_8_ = 0xe951440710637bef;
  xor_table._240_8_ = 0x330c4a5a3dce2989;
  xor_table._248_8_ = 0x81d57f6dd1652132;
  for (i = 0; i < 0x100; i = i + 1) {
    output_buf[i] = out_table[input_buf[idx_table[i]]] ^ xor_table[i];
  }
  if (lVar1 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```

各バイトについて、以下のような処理をしてますね。

```c
output_buf[i] = out_table[input_buf[idx_table[i]]] ^ xor_table[i];
```

# 解法

`input_buf`のみが未知なので、そこを復元できるように変形していきましょう。

```c
out_table[input_buf[idx_table[i]]] = output_buf[i] ^ xor_table[i]
```

ここまではいいですが、`out_table`をどうやってはがせばいいでしょう。調べればわかりますが、`out_table`は0~0xffまでを一回まで使ったテーブルとなっています。つまりインデックスと値が一対一に対応しているので、インデックスと値を反転したテーブルを用意すれば、`out_table`をはがすことができます。

テーブルは基本的にバイナリ中から抜くことができますが、xor_tableだけはデコンパイル結果からコピーするときはリトルエンディアンに注意しましょう。面倒ならgdbを使って抜くのもいいかもしれません。

```python
with open("report.pdf.enc", "rb") as f:
	enc = f.read()

idx_table = b"\x57\x85\x0e\x3b\xa5\x2f\x4c\x0a\x71\x75\xd5\x05\xff\x0b\x44\x2a\xd4\xb5\x11\xfa\x67\x23\xbd\xac\x9c\x47\x9d\x22\x5a\xef\x63\x39\xe5\xbf\x7e\x46\x64\xe3\x2e\xd1\xb9\x40\x92\x88\xa9\xa3\x02\x50\xc4\x35\x7d\x36\xcf\xe9\xb8\x96\xad\x98\x66\x74\x86\xc3\xec\x0f\x1c\x51\xe8\x1f\xc1\xd9\x16\x7f\xc0\xa8\xf4\x34\xc2\x19\x37\xea\x18\x42\x8b\xed\xda\xa1\x28\x1e\x3c\x6e\xa7\x8a\x09\x95\x94\x6d\x9e\x3d\x4a\x8f\x8c\x27\x5f\xe7\xde\xf8\xe0\x72\x6a\x82\x91\xeb\x08\xf9\xf5\xe2\x21\x2d\xe1\xf3\xc6\xba\x7a\x73\x01\x5d\xce\x3f\x59\xee\xcb\x60\x41\xd2\x58\xf6\xb4\x55\x78\x62\x70\x4e\xb2\xa4\xbb\xdb\xdc\x29\x9b\x97\xf7\x24\x76\x4b\x93\xa0\x43\xcc\x7b\xe6\x38\xa2\x65\xc5\xd8\x3a\x26\x8d\x69\xc7\xbc\x07\x25\xb1\x5e\xfb\xb0\x13\x77\xaf\x49\x99\xcd\xca\x04\xbe\x6c\xb7\x56\x6b\x17\x80\x87\x2b\x45\x81\x8e\x68\xf1\x53\x33\xa6\xfd\xd3\x0d\x2c\x14\x7c\x20\x83\x90\x4f\x1a\x89\xf0\xfe\x32\xdf\xd6\x06\x1b\xd0\xaa\xae\x79\xdd\x84\xe4\x03\x12\x9a\x6f\xab\xd7\x1d\x3e\xc9\x0c\x9f\x30\x10\x54\xb3\xf2\x15\x61\x5c\xb6\x31\x5b\x4d\xc8\xfc\x48\x52\x00"
out_table = b"\x06\x8c\x77\x86\x11\xed\x25\x89\x66\x64\x79\x7d\xc9\x0d\xa5\x99\x44\x6b\x71\x47\xaa\x9e\x1b\x0a\xc3\xbf\x1e\x6e\xa6\x82\xf0\x61\x84\x35\x42\x90\x87\xb2\xb0\xc2\x3d\xf4\x12\x73\x45\x3e\xe9\xcd\x26\x41\x33\xa4\x5b\x2d\x53\xe8\x3a\xc5\xbc\x18\xe5\xba\x81\xeb\x58\x9f\x49\xcc\x2f\xac\xcf\x8a\x0b\x48\x24\x9c\xa2\xb4\x15\xd0\x1f\x19\xd3\x16\xf3\x07\x4b\x78\x80\x34\xe2\x31\xc1\x57\x00\x7e\x5e\x70\x54\x21\x69\x9b\x46\x6a\xb6\xcb\x9a\x40\xb9\x17\x6d\x59\xfc\xea\x60\x32\xdf\x75\xe3\x62\x38\xa7\x85\xd7\x03\xf1\x83\xb5\x55\x5f\xee\xfd\xad\x0e\x6c\xa3\x20\xc0\x13\x08\x02\x5a\x72\x9d\x5d\xfb\x88\x93\xf9\x39\x74\xd8\xd2\x4f\x04\x67\x3f\xce\xe1\x4d\xd5\xca\x2c\x94\x2b\xdb\x09\x2a\x37\xe7\x95\x29\x4e\x22\x01\x0f\xdc\xd4\xc8\x56\x7a\x14\xf8\xb8\x30\x43\xa8\xa9\xf5\x8d\x5c\xab\x6f\x96\x1a\x23\x4a\x0c\x2e\x51\xd6\x92\xc7\x52\x8e\xe4\x4c\x65\x68\x97\xbb\x05\xdd\xbe\xef\x8b\xb7\x98\x76\xc4\xda\xb3\x7b\xa1\x36\xa0\x91\xaf\xf6\xfa\xe0\x10\x27\x1c\xbd\xfe\x50\xde\x7c\xf2\xb1\xae\xc6\xd9\xe6\x3c\xd1\x7f\xff\x63\x1d\xec\x3b\x8f\x28\xf7"
xor_table = b"\x72\x1e\xec\x52\x38\xe9\xb5\xc2\x46\x47\x75\x1f\x53\x0f\xea\x27\xcf\x57\xd7\x6e\x8c\x8c\x89\x2a\xf2\x86\x8a\x7b\x19\x7a\x2e\x01\xab\x15\x08\xd3\x2b\x5b\x9f\x7c\x86\xde\x5d\x98\x3c\x6f\x82\x58\xf2\xea\x85\x62\xa5\x77\xf3\x9e\x3e\x37\x10\x8b\x9e\xa0\x71\x1b\xce\x9d\x7e\x2f\xb3\x17\x01\x65\x14\x5c\x79\x2f\xad\xe1\x28\xf9\x55\x92\x3a\x69\x1f\x12\x5e\xa6\x41\xa4\xdb\xda\x47\x3b\xe3\x28\x08\x09\xe9\x9c\xfa\x22\x7c\x62\xd2\x05\x28\x86\x95\xe4\x45\x8e\xd2\xe7\xeb\x66\xed\x58\x64\x42\xba\xa9\x70\x21\xa0\x91\x51\x68\xff\x7e\xa9\x6c\x12\x33\xbb\x7a\xde\x1b\xe0\xed\xce\x7c\x04\x01\xcf\x23\x17\x36\x78\x1b\x06\xd3\x5e\x25\x5e\x98\x86\x50\x4a\x0d\x31\x0c\x39\x96\x6e\x72\x2b\xc2\x0f\x31\xdd\x4c\xd7\x44\xa9\xf9\xb7\xed\x40\xb9\x68\x73\xa6\xb0\xef\x3e\x2e\x37\x03\xb6\xe4\x4c\xcb\x5d\x83\x74\x10\xf0\x54\x62\xc1\x28\xdf\x5c\xff\xa7\x6e\x84\x59\x39\xeb\x63\xa0\x5b\x17\x3d\x97\xee\xcb\x8b\x21\x7b\x77\x98\xd5\xa9\x59\x44\x8d\x38\x70\x06\xef\x7b\x63\x10\x07\x44\x51\xe9\x89\x29\xce\x3d\x5a\x4a\x0c\x33\x32\x21\x65\xd1\x6d\x7f\xd5\x81"

inv_out_table = [0]*256
for i, ti in enumerate(out_table):
	inv_out_table[ti] = i

print(inv_out_table)

plain = b""
for i in range(0, len(enc), 256):
	output_buf = enc[i:i+256]
	input_buf = [0] * 256
	for j in range(256):
		# output_buf[i] = out_table[input_buf[idx_table[i]]] ^ xor_table[i]
		input_buf[idx_table[j]] = inv_out_table[output_buf[j] ^ xor_table[j]]
	plain += bytes(input_buf)

print(plain)

with open("repair.pdf", "wb") as f:
	f.write(plain)

```



