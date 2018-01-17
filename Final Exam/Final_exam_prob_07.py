# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:04:53 2017

@author: .LUCAS
"""

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def function_f(n):
        total_sum = 0
        for i in range(len(L)):
            total_sum += L[i]*(n**(len(L)-i-1))
        
        return total_sum
          
    return function_f
    
L = [1, 2, 3, 4]

#general_poly(L)
general_poly([1, 2, 3, 4])(10)
        
        
        