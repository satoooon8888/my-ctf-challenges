key = b";,Z,.(7TWT2$jAU2#YLZ!QE^,(D h;H\t"
answer = b"CAn_U_Re4d_A55emBly?L3t's_tRY_it"
flag = ""
for i in range(len(key)):
    flag += chr(key[i] ^ answer[i])
print(flag)


