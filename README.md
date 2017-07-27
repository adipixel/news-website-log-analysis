# Log analysis tool for a newspaper website
An internal reporting tool for a newspaper website using PostgreSQL and Python, that will use information from the database with over a million rows to discover what kind of articles the site's readers like.

### Technologies used
- Python
- PostgreSQL

### Execution Instructions
- Execute using the following command
`python log-analysis-console.py`
- The output gets printed in the file
`log-analysis-output.txt`

### Contents of the files
- `log-analysis.py` contains the methods to retrive data from the database
- `log-analysis-console.py` contains the driver code which calls methods from `log-analysis.py` and prints the results in `log-analysis-output.txt` file.
