#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:37:11 2021

@author: martin
"""

import numpy as np

a = np.genfromtxt('/mnt/c/Users/Darien N/Downloads/combined.txt',dtype=str,usecols=(0)) 
b = np.genfromtxt('/mnt/c/Users/Darien N/Downloads/combined.txt',dtype=str,delimiter='\t',usecols=(5))
c = dict(zip(a,b.tolist()))    
#print (c)
e = np.genfromtxt('/mnt/c/Users/Darien N/downloads/seq2.tabular',dtype=str,usecols=(0)) 
f = np.genfromtxt('/mnt/c/Users/Darien N/downloads/seq2.tabular',dtype=str,delimiter='\t',usecols=(int(2)))
g = dict(zip(e,f.tolist()))
h = {}
for key in g.keys():
    new_key = key.split("~~",1)[-1]
    h[key] = new_key
for old, new in h.items():
    g[new]= g.pop(old)
g1 = {}

for k in g:
    if k in c:
        g1[k] = c[k] + " "+ g[k]

#print (g1)
# from here it removes the NA log values
g2= {}

for k in g:
    if g[k] != "NA":
        g2[k] = g[k]

g3 = {}

for k in g2:
    if k in c:
        g3[k] = c[k] + " "+ g2[k]
#print(g3)

with open("seq_table.txt", "w") as o:
    for k in g2:
        if k in c:
            o.write(k+" " + c[k] +" "+ g2[k]+"\n")
