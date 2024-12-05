import random

def create_dummy():
	op = random.choice(["mov", "add", "sub", "cmp"])
	reg = random.choice(["eax", "ebx", "ecx", "edx"])
	val = random.randint(0, 0x100000000)
	asm = 'asm(".intel_syntax noprefix");\n'
	asm += f'asm("{op} {reg}, {val}");\n'
	asm += 'asm(".att_syntax");\n'
	return asm
	# return ""

flag = b"xm4s{mad_dummy_blocks_the_way!}"
dummy_len = 8000

if len(flag) % 4 != 0:
	flag += b"\x00" * (4 - len(flag) % 4)

code = """
#include<stdio.h>
int main(void) {
"""

for i in range(random.randint(dummy_len, dummy_len+1000)):
	code += create_dummy()

code += f"int fail=0;\n"
code += f"printf(\"FLAG: \");\n"
code += f"char buf[{len(flag)+1}];\n"
for i in range(random.randint(dummy_len, dummy_len+1000)):
	code += create_dummy()

code += f'scanf("%{len(flag)}s%*c", buf);\n'

for i in range(random.randint(dummy_len, dummy_len+1000)):
	code += create_dummy()

for i in range(0, len(flag), 4):
	code += f'if (*(int*)(&buf[{i}]) != {int.from_bytes(flag[i:i+4], "little")}) fail=1;\n'
	for i in range(random.randint(dummy_len, dummy_len+1000)):
		code += create_dummy()

code += """
if (fail) {
	puts("Incorrect...");
} else {
	puts("Correct!");
}
"""

code += "}"

print(code)
