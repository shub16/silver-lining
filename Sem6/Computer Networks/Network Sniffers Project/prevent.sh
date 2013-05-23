
#This script generates an alert using snort in the log file and calls ping.pl script as a subroutine

#!/bin/bash
rm /var/log/snort/alert
snort -c /etc/snort/rules/myrules.rules &		# running snort in background
sleep 10
kill $!
sleep 4
iptables -F
chmod +x script.pl
perl ping.pl 				# calling perl script
iptables -L
