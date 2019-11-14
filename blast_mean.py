#!/usr/bin/env python
import io

blast_handle = io.open("pz_blastx_yeast_top1.txt", "rU")

counter = 0
eval_sum = 0.0

for line in blast_handle:
    line_stripped = line.strip()
    line_list = line_stripped.split("\t")
    eval_str = line_list[10]

    eval_sum = eval_sum + float(eval_str)
    counter = counter + 1

blast_handle.close()

mean = eval_sum/counter
print("Mean is: " + str(mean))
