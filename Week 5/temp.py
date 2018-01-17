
shift = 3
 
original_letters = [0 for x in range(52)]

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

alpha = string.ascii_lowercase+string.ascii_uppercase

my_dict = {}

#Shifting the letters:
k=shift
for i in range(len(alphabet_lower)):
    my_dict[alphabet_lower[i]] = alphabet_lower[k]
    my_dict[alphabet_upper[i]] = alphabet_upper[k]
    print(alphabet_lower[i] + ' ' +  alphabet_lower[k])
    k+=1
    if k==len(alphabet_lower):
        k=0

#-------------------------------------------------------------------------------

msg = 'abc, def'

msg__=''
for i in range(len(msg)):
    char = msg[i]
    if (char in string.ascii_lowercase) or (char in string.ascii_uppercase):
        msg__+= my_dict[char]
    else:
        msg__+=char

print(msg__)

#-------------------------------------------------------------------------------







