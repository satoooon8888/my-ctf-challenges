from Crypto.Util.number import *
from random import getrandbits

with open("flag.txt", "rb") as f:
	flag = f.read()
	assert len(flag) == 18


p = getStrongPrime(512)
q = getStrongPrime(512)
N = p * q

m = bytes_to_long(b"the magic words are squeamish ossifrage. " + flag)

e = 7
d = pow(e, -1, (p - 1) * (q - 1))
c = pow(m, e, N)

print(f"N = {N}")
print(f"e = {e}")
print(f"c = {c}")
