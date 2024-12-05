```c
void give_monster_name(Monster* monster) {
	printf("Let's give your monster a name!\n");
	print_monster_infomation(*monster);

	printf("Input name: ");
	scanf("%s%*c", monster->name);
	
	print_monster_infomation(*monster);
	print_and_wait("OK, Nice name.");
}
```

`scanf("%s%*c", monster->name)`の部分が脆弱性です。scanfの書式文字列`%s`は文字列長を指定しないと`monster->name`を超えて入力を読み込んでしまうBuffer Over Flowが起きます。

```c
typedef struct {
	char name[16];
	int64_t hp;
	int64_t attack;
} Monster;
```

構造体`Monster`は`name`の下に`hp`と`attack`を持つため、16文字以上の入力をすると`hp`, `attack`を上書きすることができます。`12345678123456781234567812345678`などの入力をすることで`hp`, `attack`を大きな値に上書きすることで相手のHPを削り切り、フラグを得ることができます。

# 備考

☆2にしてはコードが長い？

リターンアドレスの書き換えなど実際の攻撃はいきなりの理解が難しいので、ローカル変数の書き換えでメモリ破壊に親しんでもらいたい(?)
