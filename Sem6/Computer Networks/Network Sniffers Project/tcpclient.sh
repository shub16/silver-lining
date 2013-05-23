
#This script run the tcpclient.c code for 3 seconds



gcc tcpclient.c -o tcpclient
./tcpclient 10.20.254.41 &
sleep 3
kill $!
