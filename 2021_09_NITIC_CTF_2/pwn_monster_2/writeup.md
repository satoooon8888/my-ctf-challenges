```c
	int64_t checksum = monster->hp + monster->attack;

	printf("Checksum: %ld\n", checksum);

	printf("Input name: ");
	scanf("%s%*c", monster->name);
	
	print_monster_infomation(*monster);

	printf("Checksum: %ld\n", monster->hp + monster->attack);

	if (monster->hp + monster->attack != checksum) {
		puts("Detect cheat.");
		exit(1);
	}
```

pwn monster 1と同様にBuffer Over Flowにより`hp`, `attack`を上書きできますが、チェックサムが追加されています。書き込む前後で、`monster->hp + monster->attack`が変化しているとチートをしていると判断しているようです。

`hp`, `attack`の初期値は100, 10なので書き込む前の`monster->hp + monster->attack`は110です。`monster->hp + monster->attack`が110になるように調整しつつ、都合のいい値に上書きする必要があります。

これは`hp`に0x0100000000000000, `attack`に0xff0000000000006eを入れるとうまくいきます。`monster->hp + monster->attack`は0x1000000000000006eになりますが、`int64_t`は64bit整数で溢れた分は無視されるので、結果的に0x6e=110になります。

このとき、0x0100000000000000を整数に直すと72057594037928046で0xff0000000000006eは-72057594037927936になります。attackがマイナスになるため相手にHPを与え続けることになりますが、これも`int64_t`が固定長であることを利用するといつか相手のHPが負の値になることがわかります。相手のHPが負になった瞬間に勝利するので、これでフラグが得られます。

# 備考

unprintableな入力とリトルエイディアンに慣れてもらうための問題。

そのままじゃつまらないので整数オーバーフローも足した。

