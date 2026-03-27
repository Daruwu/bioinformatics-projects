#!/usr/bin/python3

data1 = input("enter a seq: ")
data2 = int(input("Enter a k-mer: "))
data3 = int(input("Enter a d: "))

def HammingDistance(s1, s2):
    d = sum([1 for i in range(len(s1)) if s1[i]!=s2[i]])
    return d

def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ["A", "C", "G", "T"]
    neighbor= []
    suffixneighbors = neighbors(pattern[1:], d)
    for text in suffixneighbors:
        if HammingDistance(pattern[1:], text) < d:
            for x in ["A", "C", "G", "T"]:
                neighbor.append(x + text)
        else:
            neighbor.append(pattern[0] + text)

    return neighbor

def find_frequent(string, k, d):
    words = []
    neighborhood = set()
    result = []

    for i in range(len(string) - k + 1):
        words.append(string[i: i + k])

    for word in words:
        neighborhood.update(set(neighbors(word, d)))

    mmax = 0
    for i in neighborhood:
        frequenti = 0
        for c in words:
            if HammingDistance(i, c) <= d:
                frequenti += 1

        if mmax < frequenti:
            mmax = frequenti
            result = [i]
        elif mmax == frequenti:
            result.append(i)
    
    print (" ".join(result))

(find_frequent(data1, data2, data3))