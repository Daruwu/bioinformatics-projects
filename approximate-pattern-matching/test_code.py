#!/usr/bin/python3

from Bio.Seq import Seq

Pattern = input("Enter a pattern: ")
Text = input("Enter a sequence: ")
d = int(input("Enter a d-value: "))

def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

def remove_duplicates(Items):
    ItemsNoDuplicates = [] 
    for i in Items:
        if not i in ItemsNoDuplicates:
            ItemsNoDuplicates.append(i)
    return ItemsNoDuplicates

def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates 

def PatternMatching(Pattern, Genome):
    positions = [] 
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

def ReverseComplement(Pattern):
    revComp = Seq(Pattern.reverse_complement)
    return ('').join(revComp)[::-1]


#def ReverseComplement(Pattern):
#    revComp = map(complement, Pattern)
#    return ('').join(revComp)[::-1]

#def complement(Nucleotide):
#    complements = { 'A': 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
#    comp = complements[Nucleotide.upper()] 
#    return comp

def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array
    
def Skew(Genome):
    skew = {} 
    skew[0] = 0
    for i in range(1, len(Genome) + 1):
        if Genome[i-1] == 'G':
            skew[i] = skew[i-1] + 1
        elif Genome[i-1] == 'C':
            skew[i] = skew[i-1] -1
        else:
            skew[i] = skew[i-1]       
    return skew

def hammingDist(seq1, seq2):
    i = 0
    distance = 0
 
    while(i < len(seq1)):
        if(seq1[i] != seq2[i]):
            distance += 1
        i += 1
    return distance

#def HammingDistance(p, q):
#    distance = 0
#    for i in range(0, len(p)):
#        if p[i] != q[i]: distance = distance + 1
#    return distance

def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] 
    for i in range(len(Text)-len(Pattern)+1):
        if hammingDist(Text[i:i+len(Pattern)],Pattern) <= d:
            positions.append(i)
    print (str(positions).replace(',','')[1:-1])

(ApproximatePatternMatching(Pattern, Text, d))