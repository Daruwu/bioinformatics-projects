#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:37:00 2021

@author: martin
"""


import json
import numpy as np

a = np.genfromtxt('/mnt/c/Users/Darien N/Downloads/combined.txt',dtype=str,usecols=(0)) 
b = np.genfromtxt('/mnt/c/Users/Darien N/Downloads/combined.txt',dtype=str,delimiter='\t',usecols=(1,4,5))
c = dict(zip(a,b.tolist()))    

#print(c)
e = np.genfromtxt('/mnt/c/Users/Darien N/downloads/deseq2_G_corn.tabular',dtype=str,usecols=(0)) 
f = np.genfromtxt('/mnt/c/Users/Darien N/Downloads/deseq2_G_corn.tabular',dtype=str,delimiter='\t',usecols=(2))
g = dict(zip(e,f.tolist()))    

h = {}
for key in g.keys():
    new_key = key.split("~~",1)[-1]
    h[key] = new_key
    
#print(h)

for old, new in h.items():
    g[new]= g.pop(old)

list_of_matches = list(g.keys())
#print (list_of_matches)

c_copy = c.copy()
g_copy =g.copy()
list_of_dict = []
list_of_dict.append(c_copy)
list_of_dict.append((g_copy))
#print(list_of_dict)

d = {}
for match in list_of_matches:
    for ld in list_of_dict:
        d.setdefault(match,[]).append(ld.get(match, 0))
d_items=d.items()
#print(d)
with open("seq_table.txt","w") as file:
        file.write(json.dumps(d))
