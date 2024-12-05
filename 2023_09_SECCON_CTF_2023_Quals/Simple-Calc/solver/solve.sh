docker run -it \
    -e WEB_BASE_URL=http://simplecalc.seccon.games:3000 \
    -e ATTACKER_BASE_URL=https://eo89rba2rkj9j6f.m.pipedream.net \
    -p 8080:8080 \
    $(docker build -q .)
