# Log analysis project
# Author: Aditya Mhamunkar
# email: me@adityamhamukar.com
import datetime
import psycopg2


DBNAME = "news"


def get_top_three():
    query = '''select articles.title, counts from articles,
     (select sub.path_slug as paths, count(sub.path_slug) as counts from
     (select substring(path from 10) as path_slug from log where path <> '/')
     as sub GROUP BY sub.path_slug ORDER BY counts desc) as yo
     where articles.slug = yo.paths limit 3;'''
    return run_query(query)


def get_popular_authors():
    query = '''select authors.name, sum(final.counts) as sum from authors join
     (select articles.author, counts from articles join
     (select sub.path_slug as paths, count(sub.path_slug) as counts from
     (select substring(path from 10) as path_slug from log where path <> '/')
     as sub GROUP BY sub.path_slug ORDER BY counts desc) as yo
     on articles.slug = yo.paths) as final on
     final.author = authors.id GROUP BY authors.name ORDER BY sum desc;'''
    return run_query(query)


def get_err_status():
    query = '''select to_char(all_status.day, 'FMMonth FMDD, YYYY') as date,
     round(100*(red_status.count::float/all_status.counts)::numeric,1)
     as percent from (select date(time) as day, count(status) from
     log where status LIKE '4%' GROUP BY day) as red_status,
     (select date(time) as day, count(status) as counts from log GROUP BY day)
     as all_status where
     trunc(100*(red_status.count::float/all_status.counts)::numeric,1) > 1
     and all_status.day = red_status.day;'''
    return run_query(query)


def run_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results