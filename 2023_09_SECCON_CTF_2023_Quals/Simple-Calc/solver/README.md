docker run -it \
    -e WEB_BASE_URL=http://simple-calc.seccon.games:3000 \
    -e ATTACKER_BASE_URL=http://attacker.example.com \
    -p 8080:8080 \
    (docker build -q ./solver)