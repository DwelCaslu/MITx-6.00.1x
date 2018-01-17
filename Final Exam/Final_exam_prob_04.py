# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:50:37 2017

@author: .LUCAS
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    long_inc = []
    long_dec = []
    happ_dec_st = 0
    happ_inc_st = 0
    
    for i in range(len(L)):
        inc_ = [L[i]]
        dec_ = [L[i]]
        inc_st = 1
        dec_st = 1
        for j in range(i+1,len(L)):

            if L[j]>=L[j-1] and inc_st==1:
                inc_.append(L[j])
            else: 
                inc_st = -1
                
            if L[j]<=L[j-1] and dec_st==1:
                dec_.append(L[j])
            else:
                dec_st = -1
        
        if len(inc_)>len(long_inc):
            long_inc = inc_
            happ_inc_st = i
            
        if len(dec_)>len(long_dec):
            long_dec = dec_
            happ_dec_st = i
    
    #print(long_dec)
    #print(long_inc)
    
    if len(long_dec) > len(long_inc):
        the_long_sum = long_dec
    
    elif len(long_dec) < len(long_inc):
        the_long_sum = long_inc
    
    else:
        if happ_inc_st<happ_dec_st:
            the_long_sum = long_inc
        else:
            the_long_sum = long_dec
        
    #print(sum(the_long_sum))
    return sum(the_long_sum)
    
L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]   
#L = [5, 4, 10] 
longest_run(L)    
    