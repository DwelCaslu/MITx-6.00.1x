# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 14:04:49 2017

@author: .LUCAS
"""
s = 'azcbobobegghakl'

count = 0
for i in range(len(s)):
    if s[i]=='a' or s[i]=='b' or s[i]=='c' or s[i]=='d' or s[i]=='e':
        count +=1
print('Number of vowels: ',count)       