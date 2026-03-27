#!/usr/bin/python3

data = input("Enter the sequence: ")
k = int(input("Enter the kmer: "))
L = int(input("Enter the clump L: "))
t = int(input("Enter the minimum requirement t: "))

def get_clumps(k, L, t, data):
    start = 0
    answer = set()
    data_len = len(data)
    while start + L <= data_len:
        substr_dict = {}
        window = data[start:start + L]
        sub_start = 0
        wind_len = len(window)
        while sub_start + k <= wind_len:
            sub = window[sub_start:sub_start + k]
            if sub not in substr_dict:
                substr_dict[sub] = 1
            else:
                substr_dict[sub] += 1

            sub_start += 1

        start += 1
        answer_list = [key for key in substr_dict.keys() if substr_dict[key] >= t]
        for item in answer_list:
            answer.add(item)
            
    return answer

print (' '.join(get_clumps(k, L, t, data)))