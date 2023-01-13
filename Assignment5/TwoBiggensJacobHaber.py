#Jacob Haber
def two_biggens(i, j, k): 
    """Return m*m + n*n, where m and n are the two largest members of the 
    positive numbers i, j, and k. 
    >>> two_biggens(1, 2, 3) 
    13 
    >>> two_biggens(5, 3, 1) 
    34 
    >>> two_biggens(10, 2, 8) 
    164 
    >>> two_biggens(5, 5, 5) 
    50 
    """ 
    return  ([i,j,k][0:[i,j,k].index(min([i,j,k]))]+ [i,j,k][[i,j,k].index(min([i,j,k])) + 1:])[0] ** 2 + ([i,j,k][0:[i,j,k].index(min([i,j,k]))]+ [i,j,k][[i,j,k].index(min([i,j,k])) + 1:])[1] ** 2
#this looks terrible 
      
    

print(two_biggens(1, 2, 3))
print(two_biggens(5, 3, 1))
print(two_biggens(10, 2,8))
print(two_biggens(5, 5, 5))