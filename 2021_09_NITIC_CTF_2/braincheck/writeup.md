```
>,>,[>+>+<<-]>>[<<+>>-]<<[-<->]<-----[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<>+++++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<>++[<----->-]<-[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<------[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<----[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<>++++++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<--[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<>+++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<----[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<>++[<----->-]<----[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<>+++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<>++++[<----->-]<--[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<>++++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<--[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<----[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<>++++++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<-[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<>+++[<----->-]<[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<>++++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<---[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<---------[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<------[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<>+++++++[<----->-]<-[<+>[-]]>>[<<+>>-]<,[>+>+<<-]>>[<<+>>-]<<[-<->]<>++++++++++++++++++++++++++++++++++++++[<----->-]<----[<+>[-]]>>[<<+>>-]<,>>+<<<[-]<[[-]>+++++++++++++++++[<+++++>-]<++.>+++++[<+++++>-]<++.---.-.-------.>>>>-<<<<[-]]>>>>[[-]>+++++++++++++[<+++++>-]<++.>++++++++[<+++++>-]<++++.+++..>++[<----->-]<---.--.>+++[<+++++>-]<++.[-]]
```

ソースコードをみると共通部分が多く見つかります。そこで塊ごとに整理してみます。

```
>,
>,
[>+>+<<-]>>[<<+>>-]<<[-<->]<-----[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<>+++++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<>++[<----->-]<-[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<------[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<----[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<>++++++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<--[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<>+++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<----[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<>++[<----->-]<----[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<>+++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<>++++[<----->-]<--[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<>++++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<--[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<----[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<>++++++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<-[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<>+++[<----->-]<[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<>++++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<---[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<---------[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<------[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<>+++++++[<----->-]<-[<+>[-]]>>[<<+>>-]<,
[>+>+<<-]>>[<<+>>-]<<[-<->]<>++++++++++++++++++++++++++++++++++++++[<----->-]<----[<+>[-]]>>[<<+>>-]<,
>>+<<<[-]<
[[-]>+++++++++++++++++[<+++++>-]<++.>+++++[<+++++>-]<++.---.-.-------.>>>>-<<<<[-]]
>>>>[[-]>+++++++++++++[<+++++>-]<++.>++++++++[<+++++>-]<++++.+++..>++[<----->-]<---.--.>+++[<+++++>-]<++.[-]]
```

```
[>+>+<<-]>>[<<+>>-]<<[-<->]< ... [<+>[-]]>>[<<+>>-]<,
```

という構造が続いていることがわかります。[オンラインbrainf*ckデバッガ](http://moon.kmc.gr.jp/~prime/brainf_ck/env/) を使えばブレークポイントを挟んでメモリを見ることができます。3行目をこのように書き替え、入力を`nitic_ctf{hoge}`にして実行してみましょう。

```
@[>+>+<<-]>>@[<<+>>-]<<@[-<->]<@-----@[<+>[-]]@>>[<<+>>-]<,@
```

ブレークポイントごとの結果は以下のようになります。

1. `00,6e,69,00,00,00...`

   1文字目が1番地、2文字目が2番地で受け取られる (0x6e, 0x69はASCIIでそれぞれnとi)

2. `00,6e,00,69,69,00...`

   2文字目を3番地と4番地に移動させる

3. `00,6e,69,69,00,00...`

   4番地から2番地に移動させる

4. `00,05,00,69,00,00...`

   2番地-3番地を2番地に格納、3番地はクリアされる

5. `00,00,00,69,00,00...`

   2番地が-5される

6. `00,00,00,69,00,00...`

   何も起こらない

7. `00,69,74,00,00,00...`

   3番地から1番地に移動させ、2番地に3文字目が入力される

この何も起こらない6の部分は何でしょうか。コードでは`[<+>[-]]`にあたります。

このコードを解読すると、「現在位置が0でなければ現在位置-1に1を足し、現在位置を0にする」という処理であることがわかります。

実際に入力の2文字目を変えて`nhtic_ctf{hoge}`などにしてみると、0番地が1足される様子が確認できます。

そして、最後のこの部分。

```
[[-]>+++++++++++++++++[<+++++>-]<++.>+++++[<+++++>-]<++.---.-.-------.>>>>-<<<<[-]]
>>>>[[-]>+++++++++++++[<+++++>-]<++.>++++++++[<+++++>-]<++++.+++..>++[<----->-]<---.--.>+++[<+++++>-]<++.[-]]
```

これもブレークポイントを挟めばわかりますが、1番地が0であるかどうかで処理が分岐しており、`Wrong`と表示されている現在は1番地は0にはなっていません。つまり1番地を0にすれば`Correct!`と表示されるのでは？と推測できます。

4,5の処理からどう判定処理しているかを考えると、2文字目-1文字目の差を見て正しいかどうか判定していることがわかります。この差はプログラム中に埋め込まれているのでそれを取り出せばフラグが復元できます。

```python
import re

with open("source.bf", "r") as f:
	source = f.read()

diff = []

for match in re.findall(R"\[>\+>\+<<-\]>>\[<<\+>>-\]<<\[-<->\]<(.*?)\[<\+>\[-\]\]>>\[<<\+>>-\]<,", source):
	if match[0] == ">":
        # 一部for文で引き算を表現しているのでそれを考慮する
		loop_count, fraction = re.match(R">(.*?)\[<----->-\]<(.*)", match).groups()
		diff.append(len(loop_count) * 5 + len(fraction))
	else:
		diff.append(len(match))

print(diff)

flag = [ord("n")]

for i in range(len(diff)):
	flag.append((flag[-1] - diff[i]) % 0x100)

print(bytes(flag))
```
