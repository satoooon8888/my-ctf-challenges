# pwn monster 1

Author: Satoooon

Genre: pwn

Difficulty: ☆2

- dist

  配布するディレクトリ

- work

  ソルバやビルド関連を含めたディレクトリ

# 問題文

pwn monsterが完成しました！ライバルのpwnchuは最強で、バグ技を使わない限りは勝てないでしょう。

`nc example.com 9000` (ここはサーバーが用意できたら変更する)

pwn monster 1はncのみで解けるようになっています。

- Linux

  ```bash
  apt update
  apt install netcat
  ```

- Windows

  WSLでLinux環境を構築することを推奨します。

  今構築するのが難しいなら、以下の手順でncが使えるようになります。

  1. ncのリポジトリから`nc.exe`をダウンロード

  2. Windows Defenderに怒られるので`nc.exe`への検知を無効にしておく。
  3. PATHを通す

# Writeup

[writeup.md](/writeup.md)を参照