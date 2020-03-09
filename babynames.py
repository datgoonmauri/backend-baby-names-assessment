#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse

"""Baby Names exercise
Define the extract_names() function below and change main()
to call it.
For writing regex, it's nice to include a copy of the target
text for inspiration.
Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...
Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""



def extract_names(filename):
    names = []
    with open(filename) as f:
        text = f.read()
        date_match =  re.search(r'Popularity\sin\s(\d\d\d\d)', text)
        
        if not date_match:
            sys.stderr.write("No year was found")
            sys.exit(1)
        year = date_match.group(1)
        names.append(year)
        
        tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
        print(tuples)
        
    rank_names = {}
    for ranked in tuples:
        (rank, boyname, girlname) = ranked
        if boyname not in rank_names:
            rank_names[boyname] = rank
        if girlname not in rank_names:
            rank_names[girlname] = rank

    sorted_names = sorted(rank_names.keys())
    for name in sorted_names:
        names.append(name + " " + rank_names[name])
    return names

def create_parser():
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html")
    parser.add_argument(
        "--summaryfile", help="creates a summary file ", action="store_true")
    parser.add_argument("files", help="filename(s) to parse", nargs="+")
    return parser


def main():
    
  args = sys.argv[1:]
  
  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  for filename in args:
    names = extract_names(filename)
    text = '\n'.join(names)
    if summary:
        with open(filename + '.summary', 'w') as output:
         output.write(text + '\n')
    else:
      print(text)


if __name__ == '__main__':
  main()