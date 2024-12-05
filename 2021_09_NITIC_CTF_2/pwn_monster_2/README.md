# pwn monster 2

Author: Satoooon

Genre: pwn

Difficulty: ☆3

- dist

  配布するディレクトリ

- work

  ソルバやビルド関連を含めたディレクトリ

# 問題文

pwn monster 2ではバグ技を検知する機構を追加しました。

`nc example.com 9001` (ここはサーバーが用意できたら変更する)

pwn monster 2もncだけで解けますが、キーボードからの入力のみでは解けないかもしれません。いくつか方法を紹介します。

- pythonとncを使う

  ```bash
  python -c 'import sys; sys.stdout.buffer.write(b"\xef\xbe\xad\xde")' | nc example.com 9001
  ```

- echoとncを使う(Linuxのみ)

  ```bash
  echo -e "\xef\xbe\xad\xde" | nc example.com 9001
  ```

- pythonのpwntoolsを使う

  `pip install pwntools`

  ```python
  from pwn import *
  
  io = remote("example.com", "9001")
  
  payload = p64(0xdeadbeef)
  
  io.sendlineafter("Input name: ", payload)
  io.interactive()
  ```

# Writeup

[writeup.md](/writeup.md)を参照