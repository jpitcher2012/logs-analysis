#!/usr/bin/env python2.7
"""Print reports on newspaper articles."""

import psycopg2

# Connect to the database and create a cursor for getting the results
conn = psycopg2.connect("dbname=news")
cursor = conn.cursor()

# First query - get the 3 most popular articles
sql1 = """
       select a.title, count(*) as views
       from articles as a, log as l
       where l.path = CONCAT('/article/', a.slug)
       group by a.title
       order by views desc
       limit 3;
       """
cursor.execute(sql1)
results = cursor.fetchall()
print "-------------------------------------------"
print "The 3 most popular articles:"
for row in results:
    print "  ", row[0], "-", "{:,}".format(row[1]), "views"

# Second query - get the most popular authors
sql2 = """
       select au.name, count(l.id) as views
       from authors as au, articles as ar, log as l
       where au.id = ar.author
       and l.path = CONCAT('/article/', ar.slug)
       group by au.name
       order by views desc;
       """
cursor.execute(sql2)
results = cursor.fetchall()
print "-------------------------------------------"
print "The most popular authors:"
for row in results:
    print "  ", row[0], "-", "{:,}".format(row[1]), "views"

# Third query - get the days where more than 1% of requests had errors
sql3 = """
       select date, ROUND(percent::numeric,1) || '%' as percent
       from (
         select date, error/(total*1.0)*100 as percent
         from (
           select
             trim(to_char(time,'Month')) || to_char(time,' DD, YYYY') as date,
             count(id) as total,
             count(case when status = '404 NOT FOUND' then id end) as error
           from log
           group by date
         ) as x
       ) as y
       where percent > 1;
       """
cursor.execute(sql3)
results = cursor.fetchall()
print "-------------------------------------------"
print "Days where more than 1% of requests had errors:"
for row in results:
    print "  ", row[0], "-", row[1], "errors"
print "-------------------------------------------"

# Close the connection to the database
conn.close()
