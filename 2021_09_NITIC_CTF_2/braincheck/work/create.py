flag = b"nitic_ctf{esoteric?}"

code = ">,>,"
for i in range(1, len(flag)):
	d = flag[i-1] - flag[i]
	if d < 0:
		d += 0x100
	if d > 10:
		result = f">{'+' * (d // 5)}[<----->-]<{'-' * (d % 5)}"
	else:
		result = "-" * d
	# 2文字目を複製
	code += "[>+>+<<-]>>[<<+>>-]<<"
	# 2文字目-1文字目
	code += "[-<->]<"
	# 差が正しいなら0になる
	code += result
	# 正しくなければ{0}に1足す
	code += "[<+>[-]]"
	# {3}から{1}にコピー
	code += ">>[<<+>>-]<"
	# {2}に入力
	code += ","

# {4}を1に、{1}を0にしておく
code += ">>+<<<[-]<"

# {0}が1ならWrong
code += "[[-]"
d = ord("W")
for i in range(1, len("Wrong")+1):
	op = "+" if d > 0 else "-"
	d = abs(d)
	if d > 10:
		result = f">{'+' * (d // 5)}[<{op*5}>-]<{op * (d % 5)}"
	else:
		result = op * d
	code += result + "."
	if i < len("Wrong"):
		d = b"Wrong"[i] - b"Wrong"[i-1]

# Wrongなら{4}が0
code += ">>>>-<<<<[-]]"
code += ">>>>[[-]"
d = ord("C")
for i in range(1, len("Correct")+1):
	op = "+" if d > 0 else "-"
	d = abs(d)
	if d > 10:
		result = f">{'+' * (d // 5)}[<{op*5}>-]<{op * (d % 5)}"
	else:
		result = op * d
	code += result + "."
	if i < len("Correct"):
		d = b"Correct"[i] - b"Correct"[i-1]
code += "[-]]"

print(code)