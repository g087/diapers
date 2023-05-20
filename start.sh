#!/bin/bash
. .venv/bin/activate
nohup python main.py > log.txt 2>&1 &
echo $! > pid.txt
git 