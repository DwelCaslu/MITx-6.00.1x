
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    #base=int(base)
    #num = int(num)
    exp = 0
    if num-base**exp < base:
       if abs((num-base**(exp+1)))<abs((num-base**exp)):
           exp+=1
    else:
        while (num-base**exp)>base:
            exp+=1
        if abs((num-base**(exp)))==abs((num-base**(exp-1))):
            exp-=1
    #print(exp)        
    return exp

#closest_power(16, 136.0)


def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    sum = 0
    for i in range(len(listA)):
        sum = sum +listA[i]*listB[i]
    #print(sum)
    return sum
    

#listA = [1, 2, 3]
#listB = [4, 5, 6]
#dotProduct(listA, listB)

'''
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    temp=[0 for x in range(len(L))]
    j=len(L)
    for i in range(len(L)):
        j=j-1
        temp[i]=L[j]
    L=temp
    
    for i in range(len(L)):
        temp=[0 for x in range(len(L[i]))]
        j=len(L[i])
        for k in range(len(L[i])):
            j=j-1
            temp[k]=L[i][j]
        L[i]=temp
    
'''
def deep_reverse(L):
    L.reverse()
    for sublist in L:
        sublist.reverse()

       
L = [[1, 2], [3, 4], [5, 6, 7]] 
deep_reverse(L) 
print(L)  
 
    
    
