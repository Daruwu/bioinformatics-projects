#!/usr/bin/python3

from sys import argv 

text = argv[1]
pattern = argv[2]

count = 0

for i in range (0,len(text)-len(pattern)+1):
    #print (i)
    if (text[i:i+len(pattern)]) == pattern:
        count += 1
        
print (count)