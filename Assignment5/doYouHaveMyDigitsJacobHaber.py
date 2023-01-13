#Jacob Haber
#help from stack overflow
def d_in_digits(d, num): 
    """ 
    Complete d_in_digits, a function which returns True if num has the digit d & 
    returns False if num does not have the digit d. 0 is considered to have no 
    digits. You are not allowed to type cast num to a string 
 
    >>> d_in_digits(3, 123) # .Case 1 
    True 
    >>> d_in_digits(2, 123) # .Case 2 
    True 
    >>> d_in_digits(5, 123) # .Case 3 
    False 
    >>> d_in_digits(0, 0) # .Case 4 
    False 
    """ 
    "*** YOUR CODE HERE ***"
    digits = []
    #0 is not a digit
    if num == 0:
        return False
    #check digits
    while num >0:
        digits.append(num%10)
        num//=10
        #is d in the number
    return d in digits
    
    #checks if D is in num              
#case 1
print(d_in_digits(3, 123))
#case 2
print(d_in_digits(2, 123))
#case 3
print(d_in_digits(5, 123))
#case 4
print(d_in_digits(0, 0))


#Case check
d_in_digits(3,123)
d_in_digits(2,123)
d_in_digits(5,123)
d_in_digits(0,0)

