# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:42:11 2020

@author: 17426
"""
def complementary_strand(seq):
    output=''
    n=len(seq)
    i=n-1
    while i>=0:
        if seq[i]=="A":
           output=output+'T' 
        elif seq[i]=="T":
           output=output+'A'
        elif seq[i]=="C":
           output=output+'G'
        else:
           output=output+'C'
        i=i-1
    print(output)

s='ATCGTGAC'
complementary_strand(s)
        