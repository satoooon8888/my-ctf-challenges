from pwn import xor
import os
flag = "xm4s{kotoshimo_mou_nennmatsu_desune}"

if len(flag) % 4 != 0:
	flag += "\x00" * (len(flag) % 4)

print(len(flag) // 4)

key = b"\x83\x7b\x9d\x61"

encrypt = []
current = key
for i in range(len(flag)//4):
	encrypt.append(list(xor(current, flag[i*4:(i+1)*4])))
	current = xor(current, flag[i*4:(i+1)*4])


encrypt_flag = b"".join([bytes(ei) for ei in encrypt])
print(encrypt_flag)


decrypt = []
for i in range(len(encrypt_flag)//4):
	decrypt.append(list(xor(current, encrypt_flag[i*4:(i+1)*4])))
	current = xor(current, encrypt_flag[i*4:(i+1)*4])

flag = b"".join([bytes(di) for di in decrypt])

print(flag)

print("char encrypt[{}] = {{{}}};".format(len(encrypt_flag)+1, ", ".join([hex(di) for di in encrypt_flag])))

for i in range(9):
	dummy = os.urandom(len(flag))
	print("char dummy{}[{}] = {{{}}};".format(i, len(flag)+1, ", ".join([hex(di) for di in dummy])))

print("char key[{}] = {{{}}};".format(len(key)+1, ", ".join([hex(di) for di in key])))

for i in range(9):
	dummy = os.urandom(len(key))
	print("char dummy_key{}[{}] = {{{}}};".format(i, len(key)+1, ", ".join([hex(di) for di in dummy])))
