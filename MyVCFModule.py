""" Personal module for parsing VCF files. """

import io
import sys
import re

class SNP:
    """ A class representing simple SNPs"""   # Docstring
    
    def __init__(self, chrname, pos, snpid, refallele, altallele):
   	""" Constructor method """
 
        assert refallele != altallele, "Error: ref == alt at pos " + str(pos)
        self.chrname = chrname
        self.pos = pos
        self.snpid = snpid
        self.refallele = refallele
        self.altallele = altallele


    def is_transition(self):
        """ Returns True if refallele/altallele is A/G, G/A, C/T, or T/C """

        if self.refallele == "G" or self.refallele == "A":
            if self.altallele == "G" or self.altallele == "A":
                return True
        
        if self.refallele == "C" or self.refallele == "T":
            if self.altallele == "C" or self.altallele == "T":
                return True

        return False

    def is_transversion(self):
        """ Returns True if the snp is a transversion (ie, not a transition) """

        if self.is_transition():
            return False
        return True


## transition test; should not result in "Failed Test"
#snp1 = SNP("1", 12351, "rs11345", "C", "T")
#assert snp1.is_transition() == True, "Failed Test"      ## Does not error

## transversion test; should not result in "Failed Test"
#snp2 = SNP("1", 36642, "rs22541", "A", "T")
#assert snp2.is_transversion() == True, "Failed Test"    ## Does not error

## error test; should result in "Error: ref == pos at position 69835"
#snp3 = SNP("1", 69835, "rs53461", "A", "A")             ## Results in error



# ...

class Chromosome:
    """ A class representing a chromosome, which has a collection of SNPs """

    def __init__(self, chrname):
        """ Constructor """

        self.chrname = chrname
        self.locations_to_snps = dict()

    def get_name(self):
        """ Returns the chromosome name"""

        return self.name

    
    def add_snp(self, chrname, pos, snpid, refallele, altallele):
        """ Given all necessary information to add a new SNP, create
        a new SNP object and add it to the SNPs dictionary. If
        a SNP already exists at that location, or
        the given chrname doesn't match self.chrname, an error is reported. """

        ## If there is already an entry for that SNP, throw an error
        open_location = not(self.locations_to_snps.has_key(pos))
        assert open_location, "Duplicate SNP: " + self.chrname + ":" + str(pos)
        
        ## If the chrname doesn't match self.chrname, throw and error
        assert chrname == self.chrname, "Chr name mismatch!"

        ## Otherwise, create the SNP object and add it to the dictionary
        newsnp = SNP(chrname, pos, snpid, refallele, altallele)
        self.locations_to_snps[pos] = newsnp


    # ... (inside class Chromosome:)

    def count_transitions(self):
        """ Returns the number of transition snps stored in this chromosome """

        count = 0

        locations = self.locations_to_snps.keys()
        for location in locations:
            snp = self.locations_to_snps[location]
            if snp.is_transition():
                count = count + 1

        return count


    def count_transversions(self):
        """ Returns the number of transversion snps stored in this 
        chromosome """

        total_snps = len(self.locations_to_snps)
        return total_snps - self.count_transitions()




## A test chromosome
#chr1 = Chromosome("testChr")
#chr1.add_snp("testChr", 24524, "rs15926", "G", "T")
#chr1.add_snp("testChr", 62464, "rs61532", "C", "T")

## These should not fail:
#assert chr1.count_transitions() == 1, "Failed Test"
#assert chr1.count_transversions() == 1, "Failed Test"

## This should fail with a "Duplicate SNP" error:
#chr1.add_snp("testChr", 24524, "rs88664", "A", "C")


def vcf_to_chrnames_dict(filename):
    """ Create chrnames_to_chrs dictionary, given an input VCF file name
    returns the dictionary. """

    chrnames_to_chrs = dict()
    fhandle = io.open(filename, "rU")

    for line in fhandle:
        # don't attempt to parse header lines (^# matches # at start of string)
        if not(re.search(r"^#", line)):
            line_stripped = line.strip()
            line_list = re.split(r"\s+", line_stripped)

            chrname = line_list[0]
            pos = int(line_list[1])
            snpid = line_list[2]
            refallele = line_list[3]
            altallele = line_list[4]

            ## Put the data in the dictionary
            if chrnames_to_chrs.has_key(chrname):
                chr_obj = chrnames_to_chrs[chrname]
                chr_obj.add_snp(chrname, pos, snpid, refallele, altallele)
            else:
                chr_obj = Chromosome(chrname)
                chr_obj.add_snp(chrname, pos, snpid, refallele, altallele)
                chrnames_to_chrs[chrname] = chr_obj

    return chrnames_to_chrs




