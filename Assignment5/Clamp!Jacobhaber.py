#did with david shin
def clamp(ns,lo, hi ):
    """Return the value inside of the clamp defined by range x->y, if n<x return x, if n>y return y.
    >>> clamp([2,3,4], 1,3)
    [2,3,3]
    >>> clamp([7,11,365],1,3)
    [3,3,3]
    >>> clamp([11,8,5],10,6)
    [6, 6, 10]
    """
    "*** YOUR CODE HERE ***"
    for num in range(len(ns)):
        if lo <= ns[num] <=hi:
            ns[num]= ns[num]
        elif ns[num]<lo:
            ns[num] = lo
        elif ns[num]>hi:
            ns[num] = hi 
    return ns              
def clampFixed(xs,lo,hi):
    output = []
    for x in xs:
        if x> hi: output.append(hi)
        elif x < lo : output.append(lo)
        else: output.append(x)
    return output   
#case 1
print(clampFixed([2,3,4], 1,3)) #2,3,3

#case 2
print(clampFixed([7,11,365],1,3)) #3,3,3

#case 3
print(clampFixed([11,8,5],10,6)) #6,6,10