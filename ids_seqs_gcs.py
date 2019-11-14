#!/usr/bin/env python
import io


## Given a DNA (A,C,T,G) string and a 1-letter base string,
## returns the number of occurances of the base in the sequence.
def base_composition(seq, query_base):
    base_counter = 0
    seq_len = len(seq)
    
    for index in range(0, seq_len):
        seq_base = seq[index]
        if seq_base == query_base:
            base_counter = base_counter + 1

    return base_counter

## Given a DNA (A,C,T,G) sequence string, returns the GC-content as float
def gc_content(seq):
    g_cont = base_composition(seq, "G")
    c_cont = base_composition(seq, "C")
    seq_len = len(seq)
    gc = (g_cont + c_cont)/float(seq_len)
    return gc

## Open file, and loop over lines
fhandle = io.open("ids_seqs.txt", "rU")

for line in fhandle:
    linestripped = line.strip()
    linelist = line.split("\t")
    id = linelist[0]
    sequence = linelist[1]
    seqgc = gc_content(sequence)
    print(id + "\t" + str(seqgc))

fhandle.close()
