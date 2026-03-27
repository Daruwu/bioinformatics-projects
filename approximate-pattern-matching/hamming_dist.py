#!/usr/bin/python3

seq1 = input("Enter first sequence: ")
seq2 = input("Enter second sequence: ")

def hammingDist(seq1, seq2):
    i = 0
    count = 0
 
    while(i < len(seq1)):
        if(seq1[i] != seq2[i]):
            count += 1
        i += 1
    return count

print (hammingDist(seq1, seq2))

