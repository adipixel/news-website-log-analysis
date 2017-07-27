from log_analysis import get_top_three, get_popular_authors, get_err_status

def main():
  # opening a file to write the output
  f = open('log-analysis-output.txt', 'w')

  f.write('Log Analysis Project\n')

  # Searching for most popular articles
  f.write('\n\nMost popular three articles of all time\n')
  for id, path in get_top_three():
  	f.write( '\n\t"%s" - %s views' % (id, path))

  # Searching for most popular authors
  f.write('\n\nMost popular article authors of all time\n')
  for id, path in get_popular_authors():
  	f.write('\n\t%s - %s views' % (id, path))

  # Searching for errors more than 1%
  f.write('\n\nDays more than 1% of requests lead to errors\n')
  for id, path in get_err_status():
  	f.write(('\n\t%s - %s%% errors' % (id, path)).replace('      ', ' '))

  f.close()
  print "Output written to file."


if __name__ == '__main__':
  main();

