#!/bin/bash
. .venv/bin/activate
export FLASK_APP=main
export FLASK_ENV=development
nohup flask run -h localhost -p 9090 > log.txt 2>&1 &
echo $! > pid.txt
