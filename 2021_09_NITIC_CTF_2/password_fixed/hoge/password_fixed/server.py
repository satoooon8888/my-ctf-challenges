from flask import Flask, request, make_response, render_template
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
			if password[i] not in "0oO":
				return False
			continue
		if input_pass[i] in "l1I":
			if password[i] not in "l1I":
				return False
			continue
		if input_pass[i] != password[i]:
			return False
	return True

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/flag", methods=["POST"])
def search():
	if request.headers.get("Content-Type") != 'application/json':
		return make_response("invalid Content-Type Header", 415)

	input_pass = request.json.get("pass", "")
	if not fuzzy_equal(input_pass, password):
		return make_response("invalid password", 401)
	return flag

if __name__ == '__main__':
	app.run(
		debug = True,
		host = '127.0.0.1',
		port = 8080,
		threaded = True
	)
