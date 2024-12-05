# pwn monster 3

Author: Satoooon

Genre: pwn

Difficulty: ☆3

- dist

  配布するディレクトリ

- work

  ソルバやビルド関連を含めたディレクトリ

# 問題文

対策してもバグで勝つ人が多いので、pwn monster 3では勝ってもフラグを貰えないようにしました。

`nc example.com 9003` (ここはサーバーが用意できたら変更する)

ヒント: `cry()`は関数ポインタです。これを上書きすると何が起こるでしょうか。
ヒント2: PIEというセキュリティ機構が有効です。
ヒント3: `objdump`で関数のオフセットを調べることができます。

# Writeup

[writeup.md](/writeup.md)を参照