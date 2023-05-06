#!/bin/bash
. envi
nohup python main.py > /dev/null 2>&1 &
echo $! > pid.txt
