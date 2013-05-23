
#This scriot inniatializes the IP address of the source and generates all the snort rule files

#!/usr/bin/perl
system("iptables -F");
system("ifconfig eth0 > ip.txt");
open (F, "ip.txt");
$line=<F>;
$l2=<F>;
@arr = split(' ', $l2);
@ip = split(':', $arr[1]);
print @ip[1];
print "\n";
close (F);
system("rm /var/log/snort/alert");
system("rm /var/log/snort/portscan.log");  
open (F1, ">/etc/snort/rules/myrules.rules");
print F1 "alert icmp any any -> ".@ip[1]." any (itype:8; threshold: type threshold, track by_src,count 3, seconds 1; msg:\"Ping flood attack detected!\";sid:100121;)";
close (F1);
open (F2, ">/etc/snort/rules/syn.rules");
print F2 "alert tcp any any -> ".@ip[1]." any (flags:S; threshold: type threshold, track by_dst,count 20, seconds 3; msg:\"DDoS SYN flood attack detected!\";sid:12121;)";
close (F2);
open (F3, ">/etc/snort/rules/shubham.rules");
print F3 "alert icmp any any -> ".@ip[1]." any (itype:8; threshold: type threshold, track by_src,count 3, seconds 1;msg:\"Smurf attack detected!\";sid:100122;)";
close (F3);
open (F4, ">/etc/snort/rules/shub.rules");
print F4 "alert tcp any any -> ".@ip[1]." any (msg:\"worm detected#Hello... I'm the Worm\";content:\"Hello... I'm the Worm\";sid:4236353;)";
close (F4);
