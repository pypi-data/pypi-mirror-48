# xlsx2csv
Command line utility to convert xlsx file to csv

Heavily based off [Caleb Dinsmore's](https://github.com/calebdinsmore) command line utility [matillion-columns](https://github.com/calebdinsmore/matillion-columns).


# How to Run

**Before you do anything, make sure you've followed [this play](https://edusource.atlassian.net/wiki/spaces/PLAYB/pages/510460716/Create+AWS+Access+Credentials+and+Configure+AWS+CLI).**

### Installation

```bash
brew install python2
pip install --user es-xlsx2csv
```

### Run

Once you've followed these steps, you should be able to run the script, using (it may take a few seconds to run, depending on the size of the file):

`es-xlsx2csv [OPTIONS] csv_file.csv`

For more help info, run:

`es-xlsx2csv -h`