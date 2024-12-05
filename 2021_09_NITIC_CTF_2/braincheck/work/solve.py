import re

with open("source.bf", "r") as f:
	source = f.read()

diff = []

for match in re.findall(R"\[>\+>\+<<-\]>>\[<<\+>>-\]<<\[-<->\]<(.*?)\[<\+>\[-\]\]>>\[<<\+>>-\]<,", source):
	if match[0] == ">":
		loop_count, fraction = re.match(R">(.*?)\[<----->-\]<(.*)", match).groups()
		diff.append(len(loop_count) * 5 + len(fraction))
	else:
		diff.append(len(match))

print(diff)

flag = [ord("n")]

for i in range(len(diff)):
	flag.append((flag[-1] - diff[i]) % 0x100)

print(bytes(flag))