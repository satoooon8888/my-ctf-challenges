# 解法

- Part 1

  新年なんて待ってられないのでどうにかしてカウントダウンを終わらせます。

  - 想定解: main関数内のcall waitをnopで潰すか処理を飛ばす。

    本筋の解法。radare2の`wao nop`や、gdbの`set $rip=`などでできる。

  - 想定解2: 端末時間を変更する。

    あまりReversing的ではないけど関数をモックするみたいな発想で面白いと思う。

- Pert 2

  ブルートフォースなんてできないのでフラグを得る必要があります。

  - 想定解: gdbで覗く

    generate_flagとbssにあるflagからflagにフラグの文字列が生成されるのは推測できる。

    gdbでgenerate_flag後にブレークポイントを置き、flagを見ればよい。

  - 想定解2: generate_flagを解読する

    難読化してるように見えるが、実はほぼダミーコードなのでよく読めばフラグが得られる。

    だけど読める人は多分その前にgdb使ってる。