#Jacob Haber rocket
#variables 



print("what is the size of the rocket?")
rocketHeight = int(input("Enter the size of the rocket"))
talls = 2*rocketHeight
width = rocketHeight*4+2
border = '+' + '=*' *talls + '+'


#rocket top_________________________

#rocket top with input
for row in range(1,talls):
    line = ("/" * row + "**"+ "\\"* row)
    print(line.center(width))

# border top
print(border)
#rocket middle_______________
for row in range(1, rocketHeight+1):
    line = "|"+ 2*('.'*(rocketHeight-row)+ "/\\"*row +'.'*(rocketHeight-row))+"|"
    print(line)

for row in range(rocketHeight):
   line = '|' + ('.' * row+'\\/'*(rocketHeight-row)+'.'*row ) * 2 + '|'
   print(line)
    
for row in range(1, rocketHeight+1):
    line = "|"+ 2*('.'*(rocketHeight-row)+ "/\\"*row +'.'*(rocketHeight-row))+"|"
    print(line)

#bottom border

print(border)

#rocket bottom
for row in range(1,talls):
    line = ("/" * row + "**"+ "\\"* row)
    print(line.center(width))

