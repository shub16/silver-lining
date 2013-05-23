
# This script detects portscan attack by scanning the snort log file and subsequently prevent the attack, if detected, by modifying iptables.



#!/usr/bin/perl
open (F, "/var/log/snort/portscan.log");
$line=<F>;
if ($line =~ /SYN/)				#scanning the log file 
{
	print "yes\n";
	$l1=<F>;
	$l2=<F>;
	@arr = split(' ', $l2);
#	@ip1 = split(':', $arr[1]);
#	@ip2 = split(':', $arr[3]);
	print @arr[0];
	print "\n";
	print @arr[2];
	print "\n";
}
close (F);

# modifying IP table
system("iptables -A INPUT -p tcp -m state --state NEW -m recent --set && iptables -A INPUT -p tcp -m state --state NEW -m recent --update --seconds 2 --hitcount 10 -j DROP && iptables -A OUTPUT -p tcp -m state --state NEW -m recent --set && iptables -A OUTPUT -p tcp -m state --state NEW -m recent --update --seconds 2 --hitcount 10 -j DROP && iptables -A FORWARD -p tcp -m state --state NEW -m recent --set && iptables -A FORWARD -p tcp -m state --state NEW -m recent --update --seconds 2 --hitcount 10 -j DROP");



