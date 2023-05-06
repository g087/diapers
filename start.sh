#!/bin/bash
. env
nohup python main.py > /dev/null 2>&1 &
cat $1 > pid.txt
