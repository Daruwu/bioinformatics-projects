#!/usr/bin/python3

index = int(input("Enter an Index:  "))
k = int(input("Enter a k: "))

def NumberToPattern(index, k):
    bases = ['A', 'C', 'G', 'T']
    pattern = ''
    for i in range(k):
        pattern += bases[index % 4]
        index = index // 4
    return pattern[::-1]

print (NumberToPattern(index, k))
