# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 14:04:49 2017

@author: .LUCAS
"""
s = 'azcbobobegghakl'
   
best = ''          

for j in range(len(s)):
    test = s[j]    
    for i in range(j+1, len(s)):    
        if s[i]>=test[len(test)-1]:
            test = test + s[i]
        else:
            break
    if len(test)>len(best):
        best = test
    

print('Longest substring in alphabetical order is:', best)