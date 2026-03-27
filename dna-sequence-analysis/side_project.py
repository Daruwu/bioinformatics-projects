#!/usr/bin/python3

from sys import argv

DNA = input('Enter the DNA sequence for nucleotide counting: ')

a = 0
c = 0
g = 0
t = 0

for n in range (0,len(DNA)):
    if DNA[n] == 'A':
        a +=1
    if DNA[n] == 'T':
        t +=1
    if DNA[n] == 'G':
        g += 1
    if DNA[n] == 'C':
        c +=1


print("A is: " + str(a))
print("T is: " + str(t))
print("G is: " + str(g))
print("C is: " + str(c))

