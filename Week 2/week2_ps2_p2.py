# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

balance = 4773
annualInterestRate = 0.2

n = 1
last_balance = balance 
while last_balance>0:
    month = 0
    balance_test = balance
    while month<12:
        payment = 10*n
        balance_test -= payment
        interest = balance_test*(annualInterestRate/12)
        balance_test += interest
        month += 1    
        #print('Remaining balance: '+str(round(balance_test,2)))
    n +=1    
    last_balance = balance_test    
print('Lowest Payment:: '+str(payment))    