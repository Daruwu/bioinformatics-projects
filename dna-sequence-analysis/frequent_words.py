#!/usr/bin/python3

from Bio.Seq import Seq

x = Seq(input("Enter a sequence: "))
x = x.reverse_complement()
print ("\n")
print (x)