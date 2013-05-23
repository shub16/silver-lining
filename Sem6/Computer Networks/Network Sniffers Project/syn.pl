# This script detects portscan attack by scanning the snort log file and subsequently prevent the attack, if detected, by modifying iptables.


#!/usr/bin/perl
open (F, "/var/log/snort/alert");
$line=<F>;
if ($line =~ /SYN/)		# scanning snort log file for SYN keyword
{
	print "yes\n";
	$l1=<F>;
	$l2=<F>;
	@arr = split(' ', $l2);
	@ip1 = split(':', $arr[1]);
	@ip2 = split(':', $arr[3]);
	print @ip1[0];
	print "\n";
	print @ip2[0];
	print "\n";
}
close (F);

#modifying IP Tables

system("iptables -A INPUT -p tcp -s ".@ip1[0]." -d ".@ip2[0]." --tcp-flags ALL SYN -j DROP && iptables -A OUTPUT -p tcp -s ".@ip2[0]." -d ".@ip1[0]." --tcp-flags ALL SYN -j DROP && iptables -A FORWARD -p tcp -s ".@ip2[0]." -d ".@ip1[0]." --tcp-flags ALL SYN -j DROP");


