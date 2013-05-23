#This script calls port.pl script as a subroutine to prevent the attack

#!/bin/bash
iptables -F
chmod +x port.pl
perl port.pl 
iptables -L
