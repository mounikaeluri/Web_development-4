#!/usr/bin/perl  

use CGI;
use CGI::Cookie;
use DBI;

$q = new CGI;

my $host = "opatija.sdsu.edu";
my $port = "3306";
my $database = "jadrn062";
my $username = "jadrn062";
my $password = "sloop";
my $database_source = "dbi:mysql:$database:$host:$port";


my $dbh = DBI->connect($database_source, $username, $password) 
or die 'Cannot connect to db';
#send a blank cookie.  You must insert this into the header before
#printing anything.  Also, using the CGI module makes printing
#content-type: text/html redundant.

my $cookie = $q->cookie(-name=>'jadrn062',-value=>'',-path=>'/');
print $q->header(-cookie=>$cookie);
print <<END_CONTENT;
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
	<title>Cookie Reader</title>
        	<meta http-equiv="content-type"
                		content="text/html;charset=utf-8" />
            	<meta http-equiv="Content-Style-Type" content="text/css" />
	<link rel="stylesheet" type="text/css"  href="http://jadran.sdsu.edu/~jadrn062/proj4/proj4.css" />
				</head>

<body>
    <div>
            <h1>Thankyou For Ordering from Bertha's Deluxe Chololates</h1>
<h3>Your order is on the way, it would take up to 6-7 business days</h3>
END_CONTENT
my %cookies = $ENV{COOKIE};


print "<table id='read'>\n";
my ($key, $value, $value1);
     
%cookies = CGI::Cookie->fetch;


my $v = $q->cookie('jadrn062');
   
@rows = split('\|\|',$v);
foreach $row (@rows) {
    ($sku, $qty) = split('\|',$row);
     
my $statement = "INSERT INTO sales VALUES('$sku','$qty');";
    


my $sth = $dbh->prepare($statement);
$sth->execute();


    } 
my ($key, $value);

 print "<tr id='read'>\n";
 print "<td id='read'>Key</td>\n";
  print "<td id='read'>Value1</td>\n";
   print "<td id='read'>Value2</td>\n";
  
foreach $key ($q->param) {

    print "<tr id='read'>\n";
	print "<td id='read'>$key</td>\n";
    foreach $value ($q->param($key)) {
        print "<td id='read'>$value</td>\n";
        }
    print "</tr>\n";
}
print "</tr>\n";
print "</table>\n";
print "</div>\n";
print "</body>\n";
print "</html>\n";

