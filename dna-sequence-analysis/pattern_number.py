#!/usr/bin/python3

pattern = input("Enter a Pattern: ")

def PatternToNumber(pattern):
    seq = {'A':0, 'C':1, 'G':2, 'T':3}
    k = len(pattern)
    num = 0
    for i in range(k):
        num += seq[pattern[i]] * pow(4, k-i-1)
    return num

print (PatternToNumber(pattern))