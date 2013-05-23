# This script detects smurf attack by scanning the snort log file and subsequently prevent the attack, if detected, by modifying iptables.

#!/usr/bin/perl
open (F, "/var/log/snort/alert");
$line=<F>;
if ($line =~ /Smurf/)			# scanning the log file for Smurf keyword
{
	print "yes\n";
	$l1=<F>;
	$l2=<F>;
	@arr = split(' ', $l2);
	print @arr[1];
	print "\n";
	print @arr[3];
	print "\n";
}
close (F);
# Modifying the Iptables
system("iptables -A INPUT -p ICMP -s ".@arr[1]." -d ".@arr[3]." -j DROP && iptables -A OUTPUT -p ICMP -s ".@arr[3]." -d ".@arr[1]." -j DROP && iptables -A FORWARD -p ICMP -s ".@arr[3]." -d ".@arr[1]." -j DROP");


