#jacob haber letters

from re import S
#variables

size = int(input("Enter the size of the letters"))

#if size is 2 small or will cause error set size to 5
if size <= 3 :
    size = 5
    print("Size is to small or will cause an error setting size to 5")

symbol = input("pick a character you want.(any number, letter, or special character besides(\\)")
width = size*2+1





#J top______________________
for row in range(1,size):
   print(symbol*size*2)

#J middle______________________
for row in range(1,size*2-2):
    line =symbol * size
    print(line.center(width))

#J bottom

#print(symbol*(size+3))
#print( " "+symbol*(size+2) )

for row in range(1,size-2):
    line = " "*(row)  + symbol *(size+(row-1) )
    print(line)
   

#L

print(" ")

for row in range(1,size):
    line = symbol*size
    print(line)

for row in range(1,size-1):
    line = symbol*(size*2)
    print(line)    

#H

print(" ")

for row in range (1,size):
    line = symbol*size + "   " + symbol*size
    print(line)

for row in range(1,size-2):
    line = symbol*(2*size+3)
    print(line)

for row in range (1,size):
    line = symbol*size + "   " + symbol*size
    print(line)
