#!/usr/bin/perl -w
foreach(@ARGV)
{
	$cos = $cos . $_;
}
print $cos . "\n\n";
$cos =~ s/(\s)\1+/$1/g;
print $cos . "\n"; 
