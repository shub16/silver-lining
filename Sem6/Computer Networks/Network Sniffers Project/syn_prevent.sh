#This script calls syn.pl script as a subroutine


#!/bin/bash
iptables -F
chmod +x syn.pl
perl syn.pl 		# calling perl script
iptables -L

