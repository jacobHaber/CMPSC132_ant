def lacer(first, second):
    """ laces together two strings
    >>> lacer('cat','dog')
    'cdaotg'
    >>> lacer('dog','cat')
    'dcoagt'
    >>> lacer('snw', 'adich')
    'sandwich'
    """
    answer = "" 
    for i in range (len(second)):
        if i < (len(first)):
            answer += first[i]
            answer += second[i]
        else:
            answer += second[i:]    
    return answer 
#run stuff
print(lacer('cat','dog'))
print(lacer('dog','cat'))
print(lacer('snw', 'adich'))  

def delacer(word):
    """splits a word in two following an alternating
     pattern abababababa...... -> aaaaaa.... and bbbbb....
     >>> delacer('sugarhigh')
     ('sgrih', 'uahg')
     >>> delacer('dcoagt')
     ('dog', 'cat')
     >>> delacer('ababababab')
     ('aaaaa', 'bbbbb')
     """
    first = ""
    second = ""

    answer = ""
    for x in range(len(word)):
        if x % 2 == 0:
            first += word[x]
        if x % 2 == 1: 
            second += word[x]    

    return first + " "+ second 
print(delacer("sugarhigh"))
print(delacer(lacer('aaa','bbba')))




