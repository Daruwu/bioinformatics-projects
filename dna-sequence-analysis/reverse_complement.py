#!/usr/bin/python3

pattern = input("Enter a pattern: ")
text = input("Enter a sequence: ")

def PatternCount(text, pattern):
    position = []
    for i in range(0,len(text)-len(pattern) + 1):
        if text[i:len(pattern)+ i] == pattern:
            position.append(i)
    return ''.join(str(position).split(','))[1:-1]

print (PatternCount(text, pattern))