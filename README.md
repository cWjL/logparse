# logparse

Search through a single or a entire directory of log files (.log extension) and return those lines containing key words passed at runtime.<br />

Results will be in ```file name processed::line::log data``` format and saved as ```log_parse.txt``` to the current directory.

**Package Requirements:**

&nbsp;&nbsp;none

**System Requirements:**

&nbsp;&nbsp;Python 3

**Usage:**
```
usage: logparse.py [-h] [-i IN_FILE] [-r IN_DIR] -a ARGUMENTS

optional arguments:
  -h, --help    show this help message and exit
  -i IN_FILE    Process this file only
  -r IN_DIR     Process all files in this directory

required arguments:
  -a ARGUMENTS  Comma separated list of keywords to search for
```
