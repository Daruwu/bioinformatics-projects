
#!/usr/bin/python3

from Bio.SeqIO import parse
from Bio.SeqUtils import GC

max_gc = 0
for x in parse ("rosalind_gc (1).txt", "fasta"):
    
    if (GC(x.seq)) > max_gc:
        max_record = x.id
        max_gc = GC(x.seq)

print (max_record)
print (max_gc)

from sys import argv

string = argv[1]
k = int(argv[2])
kmer = ""
count = 0 
FrequentPattern = []

def FrequentWords (string,k):
    for i in range (len(string)-(k)+1):
        kmer = string[i: i+k]
        c = 0
        for i in range (len(string)-len(kmer)+1):
            if (string[i:i+len(kmer)]) == FrequentPattern:
                c += 1
            else:
                continue
        count.extend([c])
    print (count)
    if count[i] == max(count):
        FrequentPattern.extend([kmer])
    return FrequentPattern
        
FrequentWords(string, k)
        