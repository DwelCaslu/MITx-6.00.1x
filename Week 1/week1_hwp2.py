# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 14:04:49 2017

@author: .LUCAS
"""
s = 'azcbobobegghakl'

count = 0
for i in range(len(s)-2):
    if s[i]=='b' and s[i+1]=='o' and s[i+2]=='b':
        count +=1
print('Number of times bob occurs is: ',count)       