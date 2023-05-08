#!/bin/bash
. envi
nohup python main.py > log.txt 2>&1 &
echo $! > pid.txt
