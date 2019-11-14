#!/usr/bin/env python
import sys

if(sys.stdin.isatty()):
    print("Usage: cat <annotation file> | ./countannots.py")
    quit()

ids_to_counts = dict()

# Parse input
for line in sys.stdin:
    line_list = line.strip().split("\t")
    seqid = line_list[0]
    if ids_to_counts.has_key(seqid):
        ids_to_counts[seqid] = ids_to_counts[seqid] + 1
    else:
        ids_to_counts[seqid] = 1

# Print dict contents
ids_list = ids_to_counts.keys()
for seqid in ids_list:
    count = ids_to_counts[seqid]
    print(str(count) + "\t" + seqid)


