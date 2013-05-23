
# This script runs the tcpserver code 


#!/bin/bash
gcc tcpserver.c -o tcpserver
./tcpserver &

sleep 20
kill $!

sleep 3

