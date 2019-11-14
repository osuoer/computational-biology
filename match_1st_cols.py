#!/usr/bin/env python
import sys
import io

if sys.stdin.isatty() or len(sys.argv) != 2:
    print("Usage: cat <go_nums_list> | ./extract_GO_matching_ids.py <GO_file>")
    print("This script extracts lines from <GO_file> where the first ")
    print(" column of <go_nums_list> is present in the first column ")
    print(" of <GO_file>")
    quit()

## Build IDs wanted dictionary
ids_wanted = dict()
for line in sys.stdin:
    line_stripped = line.strip()
    line_list = line_stripped.split("\t")
    id = line_list[0]
    ids_wanted[id] = "present"

## Loop over the file, print the lines that are wanted
fhandle = io.open(sys.argv[1], "rU")
for line in fhandle:
    line_stripped = line.strip()
    line_list = line_stripped.split("\t")
    id = line_list[0]
    # Is the ID one of the ones we want? 
    if ids_wanted.has_key(id):
        print(line_stripped)

fhandle.close()


