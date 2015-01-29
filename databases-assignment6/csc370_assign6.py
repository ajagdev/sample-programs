#!/usr/bin/python2.7

import psycopg2
import sys

user = filename = raw_input('Enter user: \n')
passw = filename = raw_input('Enter password: \n')
pid = str(sys.argv[1])

conn_string = "host='w.cs.uvic.ca' dbname='imdb' user='%s' password='%s'" %(user, passw)

try:
	conn = psycopg2.connect(conn_string)
except:
	print "Unable to connect to database"

cur = conn.cursor()

cur.execute("select * from abhi_myfunc('%s')" %pid)
rows = cur.fetchone()
print """<html>
	<head>
 	<title>Search</title>
	</head>
	<body>
	<table border="1">"""
print "<tr><th>id</th><th>year</th><th>rank</th><th>votes</th></tr>"

while rows is not None:
	
	print "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
        rows[0], rows[1], rows[2], rows[3])
	rows = cur.fetchone()
	
print """</table>
</body></html>"""