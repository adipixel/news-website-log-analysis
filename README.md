# Log analysis tool for a newspaper website
An internal reporting tool for a newspaper website using PostgreSQL and Python, that will use information from the database with over a million rows to discover what kind of articles the site's readers like.

### Technologies used
- Python
- PostgreSQL
- VituralBox
- Vagrant

### Execution Instructions
- Load the database from the database file using following command
`psql -d news -f newsdata.sql`
- Execute using the following command
`python log-analysis-console.py`
- The output gets printed in the file
`log-analysis-output.txt`

### Contents of the files
- `log-analysis.py` contains the methods to retrive data from the database
- `log-analysis-console.py` contains the driver code which calls methods from `log-analysis.py` and prints the results in `log-analysis-output.txt` file.

### Output

```
Most popular three articles of all time

	"Candidate is jerk, alleges rival" - 338647 views
	"Bears love berries, alleges bear" - 253801 views
	"Bad things gone, say good people" - 170098 views

Most popular article authors of all time

	Ursula La Multa - 507594 views
	Rudolf von Treppenwitz - 423457 views
	Anonymous Contributor - 170098 views
	Markoff Chaney - 84557 views

Days more than 1% of requests lead to errors

	July 17, 2016 - 2.3% errors

```
