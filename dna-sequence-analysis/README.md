#!/usr/bin/python3

text = input("Enter a sequence: ")
k = int(input("Enter a k value: "))

def GenerateArray(k):
    bases = ['A', 'C', 'G', 'T']
    array = bases
    for n in range(k-1):
        array = [i+j for i in array for j in bases]
    return array

def PatternCount(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

def ComputingFrequencyArray(text, k):
    kmers = GenerateArray(k)
    for pattern in kmers:
        print(PatternCount(text, pattern), end=" ")

(ComputingFrequencyArray(text, k))