
# This script detects WORM attack by scanning the snort log file and subsequently prevent the attack, if detected, by modifying iptables.



#!/usr/bin/perl
open (F, "/var/log/snort/alert");
$line=<F>;
if ($line =~ /worm/)		#scanning the snort log file for worm keyword
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

#modifying Iptables
$str="iptables -A INPUT -p tcp -s ".@ip1[0]." -d ".@ip2[0]." \-m string \-\-algo bm \-\-string \"Hello... I\'m the Worm\" -j DROP && iptables -A OUTPUT -p tcp -s ".@ip2[0]." -d ".@ip1[0]." \-m string \-\-algo bm \-\-string \"Hello... I\'m the Worm\" -j DROP && iptables -A FORWARD -p tcp -s ".@ip2[0]." -d ".@ip1[0]." \-m string \-\-algo bm \-\-string \"Hello... I\'m the Worm\" -j DROP";
system($str);
