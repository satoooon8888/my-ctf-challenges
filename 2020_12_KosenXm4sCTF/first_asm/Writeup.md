# 解法

check_flag.sでフラグが正しいかどうか判定しているので、check_flag.sを見てみる。

ざっとラベルを見ると、for文の中にif文があるような構造であることがわかる。

最初から見ると、`mov QWORD PTR [rbp - 0x8], rdi` でrdi=第一引数に入ってくるinputのアドレスがrbp-0x8に格納されている。この変数を仮にinputと置く。

また`mov QWORD PTR [rbp - 0x10], 0`で、もう一つ変数が用意されていることがわかる。

.for_endにある`add QWORD PTR [rbp - 0x10], 1`から、`[rbp - 0x10]`は恐らくforのカウントに使うiのような変数であることが察せられる。このことから`[rbp - 0x10]`を仮にiと置いてみる。

また`cmp QWORD PTR [rbp - 0x10], 32`から、ループを32回繰り返すこともわかる。

for文の中を見てみる。段落ごとに処理をまとめると、

1. `mov cl, BYTE PTR [input + i]`

2. `mov dl, BYTE PTR [key + i]`

3. `xor cl, dl`

4. `mov dl, BYTE PTR[answer + i]`

5. `cmp cl, dl;`

6. `jne .if_false`

となっている。ここで、`BYTE PTR [input + i]`とは何か？と考えてみる。

- inputは文字列のアドレスで、そのアドレスからiの分進んだ場所を指している。

- BYTEで読みこむのは1byteで、これはchar型のサイズと等しい。

ということを考えると、inputのi番目の文字を表していることがわかる。C言語に直すと`input[i]`である。

これを基に、疑似的にC言語に直してみる。

```c
cl = input[i];
dl = key[i];
cl ^= dl;
dl = answer[i];
if (cl != dl) goto if_false
```

input[i]とkey[i]をXORして、結果がanswer[i]でなかったらif_falseに飛ぶということがわかった。

XORにはA XOR B = CのときA = B XOR Cが成り立つ性質がある。

つまり、key[i]とanswer[i]をXORすれば必要なinput[i]が求まるのではないか？と考える。

[そのようなプログラム](./solve.py)を書くと、フラグが得られる。