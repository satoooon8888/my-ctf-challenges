# 解法

ダミーコードがめちゃくちゃ入っているのでどうにかしてダミーコードを除外して読む必要があります。

ここでダミーコードを正規表現なりで削除したくなりますが、バイナリ内のオフセットが変わってしまうのでそれも調整する必要がありとても面倒くさいです。

ダミーコードを消すことはせずに、逆アセンブルした結果からダミーコードを除く方が早いです。

objdumpの結果からgrep -vでダミーコードを除いてしまいましょう。

`lea    rax,[rbp-0x30]` ~ `je`までが一塊の処理のようですが、肝心の判定部分が見えません。

何かが隠れてそうなので、radare2などのツールでその処理の周辺を確認してみます。

すると、`je`の前に`cmp eax, 0xdeadbeef`という命令が見つかります。

この4byteをASCIIコードで直してみるとフラグの断片になります。

この操作を全ての塊に対してしていけば、フラグが手に入ります。



# コメント

ダミーコードをテーマとした問題を出したかったけど、Reversing要素が少なくなってしまった...