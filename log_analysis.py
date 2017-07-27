# Log analysis project
# Author: Aditya Mhamunkar
# email: me@adityamhamukar.com
import datetime
import psycopg2
import bleach


DBNAME = "news"

def get_top_three():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	query = "select articles.title, counts from articles, (select sub.path_slug as paths, count(sub.path_slug) as counts from (select substring(path from 10) as path_slug from log where path <> '/') as sub GROUP BY sub.path_slug ORDER BY counts desc) as yo where articles.slug = yo.paths limit 3;"
	c.execute(query)
	TOP_THREE = c.fetchall()
	return TOP_THREE
	db.close()

def get_popular_authors():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	query = "select authors.name, sum(final.counts) as sum from authors join (select articles.author, counts from articles join (select sub.path_slug as paths, count(sub.path_slug) as counts from (select substring(path from 10) as path_slug from log where path <> '/') as sub GROUP BY sub.path_slug ORDER BY counts desc) as yo on articles.slug = yo.paths) as final on final.author = authors.id GROUP BY authors.name ORDER BY sum desc;"
	c.execute(query)
	TOP_AUTH = c.fetchall()
	return TOP_AUTH
	db.close()

def get_err_status():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	query2 = "select to_char(all_status.day, 'Month DD, YYYY') as date, trunc(100*(red_status.count::float/all_status.counts)::numeric,1) as percent from (select date(time) as day, count(status) from log where status LIKE '4%' GROUP BY day)as red_status, (select date(time) as day, count(status) as counts from log GROUP BY day) as all_status where  trunc(100*(red_status.count::float/all_status.counts)::numeric,1) > 1 and all_status.day = red_status.day;"
	c.execute(query2)
	ERR_STATUS = c.fetchall()
	return ERR_STATUS
	db.close()