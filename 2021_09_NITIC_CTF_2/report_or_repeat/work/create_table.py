from random import shuffle, randint

block_len = 256

xor_table = [randint(0, block_len-1) for i in range(block_len)]

substitution_table = list(range(block_len))
shuffle(substitution_table)

idx_table = list(range(block_len))
shuffle(idx_table)

with open("xor_table.csv", "w") as f:
	f.write(",".join(map(str, xor_table)))

with open("substitution_table.txt", "w") as f:
	f.write('"' + "".join(map(lambda n: f"\\x{n:02x}", substitution_table)) + '"')

with open("idx_table.csv", "w") as f:
	f.write(",".join(map(str, idx_table)))
