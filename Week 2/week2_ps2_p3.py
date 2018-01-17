# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

balance = 320000
annualInterestRate = 0.2


monthlyInterestRate = annualInterestRate/12
lower_bound = balance/12
upper_bound = balance*((1+monthlyInterestRate)**12)/12
payment = (lower_bound+upper_bound)/2

last_balance = balance 
while abs(last_balance)>0.01:
    month = 0
    balance_test = balance
    while month<12:
        balance_test -= payment
        interest = balance_test*(annualInterestRate/12)
        balance_test += interest
        month += 1    
        #print('Remaining balance: '+str(round(balance_test,2)))        
    last_balance = balance_test 
    if last_balance>0:
        lower_bound=payment
    else: 
        upper_bound=payment
    payment = (lower_bound+upper_bound)/2
print('Lowest Payment:: '+str(round(payment,2)))    