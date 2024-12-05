#!/usr/local/bin/python3
from Crypto.Util.number import *
from base64 import b64encode, b64decode

with open("./primes.txt", "rb") as f:
	p, q = map(int, f.read().split())

assert p > 2 ** 1023
assert q > 2 ** 1023

N = p * q
e = 65537
d = pow(e, -1, (p-1) * (q-1))

with open("./flag.txt", "rb") as f:
	flag = f.read()

def encrypt(m):
	return long_to_bytes(pow(bytes_to_long(m), e, N))

def decrypt(c):
	return long_to_bytes(pow(bytes_to_long(c), d, N))

def main():
	flag_c = encrypt(flag)
	print(f"(N, e) = ({N}, {e})")
	print(f"encrypted FLAG is {b64encode(flag_c).decode()}")
	print()
	print("Decode your ciphertext!")
	c = input("base64: ").encode()
	m = decrypt(b64decode(c))
	if m != flag:
		print(f"Your plaintext is {b64encode(m).decode()}")
	else:
		print("I don't decrypt FLAG!")


main()