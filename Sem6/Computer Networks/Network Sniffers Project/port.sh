#This script takes command line argument: IP address of the target machine and generate a portscan attack on it using nmap tool.


#!/bin/bash
nmap $1 &			# generating portscan attack

sleep 5
kill $!

sleep 3
