#!/usr/bin/env python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

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
def get_file_content(filename):
  try:
    with open(filename) as f:
      return f.read()
  except:
    print("error in opening file", filename)
    sys.exit(1)

def get_year(string):
  match = re.search(r'Popularity\sin\s(\d\d\d\d)', string)
  if not match:
    print("No year found", file=sys.stderr)
    sys.exit(1)
  return match.group(1)

def put_in_names(d, name, rank):
  #if names's new or newer rank is lower put it in the dict
  if (name not in d) or (name in d and d[name] > rank):
    d[name] = rank

def get_names(string):
  names_dict = {}
  matches = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', string)

  for rank, boy, girl in matches:
    put_in_names(names_dict, boy, rank)
    put_in_names(names_dict, girl, rank)

  sorted_names = sorted(list(names_dict))
  
  names_list = [item + " " + str(names_dict[item]) for item in sorted_names]
  return names_list




def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  cont = get_file_content(filename)
  year = get_year(cont)
  names = get_names(cont)
  return [year] + names


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  out = None
  for fname in args:
    names = extract_names(fname)
    if summary:
      out = open(fname + '.summary', "w")

    string = "\n".join(names) + "\n"
    print(string, file=out)
  
if __name__ == '__main__':
  main()
