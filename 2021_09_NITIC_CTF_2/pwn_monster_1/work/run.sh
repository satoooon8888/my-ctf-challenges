#/bin/bash -x
make
docker-compose up --build --remove-orphan
