#!/bin/bash
. .venv/bin/activate
nohup python main.py &
echo $! > pid.txt