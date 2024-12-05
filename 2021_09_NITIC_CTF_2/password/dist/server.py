from flask import Flask, request, make_response
import string
import secrets

password = "".join([secrets.choice(string.ascii_letters) for _ in range(32)])

print("[INFO] password: " + password)

with open("flag.txt") as f:
	flag = f.read()


def fuzzy_equal(input_pass, password):
	if len(input_pass) != len(password):
		return False

	for i in range(len(input_pass)):
		if input_pass[i] in "0oO":
			c = "0oO"
		elif input_pass[i] in "l1I":
			c = "l1I"
		else:
			c = input_pass[i]
		if all([ci != password[i] for ci in c]):
			return False
	return True

app = Flask(__name__)

@app.route("/")
def home():
	html = """
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>test page</title>
	</head>
	<body>
		<h1>Do you want the flag?</h1>
		<p>password: <input type="text" id="password"></p>
		<p><button id="submit">Submit</button></p>
		<pre id="response"></pre>

		<script>
			document.getElementById("submit").onclick = () => {
				const data = {"pass": document.getElementById("password").value}
				fetch('/flag', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json',
					},
					body: JSON.stringify(data),
				})
				.then(async (res) => document.getElementById("response").innerHTML = await res.text())
			};
		</script>
	</body>
	</html>
	"""
	return make_response(html, 200)

@app.route("/flag", methods=["POST"])
def search():
	if request.headers.get("Content-Type") != 'application/json':
		return make_response("Content-Type Not Allowed", 415)

	input_pass = request.json.get("pass", "")
	if not fuzzy_equal(input_pass, password):
		return make_response("invalid password", 401)
	return flag


app.run(port=8080)
