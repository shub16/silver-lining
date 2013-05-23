#This script calls smurf.pl script as a subroutine

#!/bin/bash
iptables -F
chmod +x smurf.pl
perl smurf.pl 
iptables -L
