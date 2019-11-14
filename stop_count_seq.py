#!/usr/bin/env python
import io

fhandle = io.open("seq.txt", "rU")
seq = fhandle.readline()
seq = seq.strip()

stop_counter = 0
for index in range(0, len(seq) - 3 + 1):
    codon = seq[index:index + 3]
    #print(codon)
    if codon == "TAG" or codon == "TAA" or codon == "TGA":
        stop_counter = stop_counter + 1

print(stop_counter)
