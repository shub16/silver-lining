
#This script calls worm.pl script as a subroutine to prevent the attack


#!/bin/bash

kill $!
sleep 4

iptables -F
chmod +x worm.pl
perl worm.pl 
iptables -L
