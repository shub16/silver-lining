#!/usr/bin/perl
if (-e "/var/log/snort/alert")
{
	open (F, "/var/log/snort/alert");
	$line=<F>;
	if ($line =~ /SYN/)
	{
		print "Syn Attack Detected!!!\n";
	}
	if ($line =~ /Ping/)
	{
		print "Ping Attack Detected!!!\n";
	}
	if ($line =~ /worm/)
	{
		print "Worm Attack Detected!!!\n";
	}	
	if ($line =~ /Smurf/)
	{
		print "Smurf Attack Detected!!!\n";
	}
	close (F);
}
if (-e "/var/log/snort/portscan.log")
{
	open (F1, "/var/log/snort/portscan.log");
	$line=<F1>;
	$line=<F1>;
	$line=<F1>;
	if ($line =~ /Portscan/)
	{
		print "Portscan Attack Detected!!!\n";
	}
	close(F1)
}
