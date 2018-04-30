#! /usr/bin/env python3

# importing postgreSQL  database module
import psycopg2

DBNAME = "news"


# the most popular three articles of all time
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("select right(log.path,- 9), count(path) as num from log where path like \
          '/article/%' and status like '2%' group by path order \
          by num desc limit 3")
posts = list(c)
print(" the most popular three articles of all time")
for article in posts:
    print "     %s: %s views" % (article[0], article[1])

db.close()

print("\n")

# the most popular article authors of all time
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("select (select authors.name from authors where id = articles.author), \
          count(right(log.path,- 9)) from log join articles\
          on articles.slug = right(log.path,- 9) and status like \
          '2%' group by name order by count desc")
posts = list(c)
print(" the most popular article authors of all time")
for article in posts:
    print "     %s: %s views" % (article[0], article[1])

db.close()

print("\n")

# days when more than 1% of requests lead to errors
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("select * from (select a.day, round(cast((100*b.hits) as numeric) /\
          cast(a.hits as numeric), 2) as error from (select date(time) as\
          day, count(*) as hits from log group by day) as a inner join \
          (select date(time) as day, count(*) as hits from log where status\
          like '4%' group by day) as b on a.day = b.day)as\
          t where error > 1.0")
posts = list(c)
print(" days when more than 1% of requests lead to errors")
for article in posts:
    print "     %s: %s percent" % (article[0], article[1])

db.close()
