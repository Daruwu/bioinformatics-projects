#!/usr/bin/python3


text = input("Enter a sequence: ")
k = int(input("Enter a k: "))

def PatternCount(text, pattern):
    count = 0
    for i in range(0,len(text)-len(pattern) + 1):
        if text[i:len(pattern)+ i] == pattern:
            count += 1
    return (count)

def FrequentWords(text, k):
    FrequentPatterns = []
    count = [0]*( len(text)-k+1)
    for i in range(0, len(text) - k + 1):
        pattern = text[i : i +k ]
        count[i] = PatternCount(text, pattern)
    maxCount = max(count)
    
    for i in range( len(text) - k + 1):
        if count[i] == maxCount:
            FrequentPatterns.append(text[i:i+k])
    results = set(FrequentPatterns)
    return (" ".join(results))
    
print (FrequentWords (text, k)) 