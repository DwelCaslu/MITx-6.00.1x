# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = 0
while month<12:
    payment = monthlyPaymentRate*balance
    balance -= payment
    interest = balance*(annualInterestRate/12)
    balance += interest
    month += 1    
    #print('Remaining balance: '+str(round(balance,2)))
    
print('Remaining balance: '+str(round(balance,2)))
    