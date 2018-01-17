# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:36:06 2017

@author: .LUCAS
"""
          
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    mand_num = ""
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
          
    us_num_int = int(us_num)  
    
    if us_num_int<=10:
        mand_num = trans[us_num]
        
    elif us_num_int>10 and us_num_int<=19:
        mand_num = trans['10'] +' '+ trans[us_num[1]]
        
    else:
         mand_num = trans[us_num[0]] + ' ' + trans['10'] 
         if us_num[1]!='0':
             mand_num = mand_num + ' ' + trans[us_num[1]]

    return mand_num 

convert_to_mandarin('16')

         