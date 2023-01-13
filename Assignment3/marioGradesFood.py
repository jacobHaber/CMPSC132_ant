import math
#jacob haber

#problem 1

#enter the level you want to check
level = input("Enter the level you want to beat: ")
# level = level[1:-1]
pos = 0

moves = ''

#loop through lvl
while pos < len(level) :
    #when mario is at end of lvl stop checking
    if pos == len(level)-1:
        break

    #mario moves one space
    if level[pos+1] == '_':
        pos += 1
        moves += 'step '

    #boo infront of mario and can only jump
    elif level[pos + 2] == '_':
        moves += 'jump '
        pos += 2
    
    #mario didn't have a mushroom
    else:
        moves = 'WRONG'
        break    

print(moves)

#original attempt before asking friend how to do it______________
    # if level[pos+1] == '_':  
    #     moves += 'step '
    #     pos +=1
    # if level[pos+1] == 'B':
        
    #     if level[pos+2]  == 'B':
    #         moves += 'Wrong'
    #         break

    #     if level[pos+2] == '_':
    #         moves += 'jump '
    #         pos += 2
        # else:
        #     moves += "WRONG "
        # elif pos =='_B':
        #     moves+= 'Jump '
        # elif pos == 'B_':
        #     moves +='   
               

#problem 2

#Variables
students = ["Bart","Kerny","Milhouse","Martin","Dolph"] 

grades   = [72.5,     79.5,     92.75,  99.999,   84.5]   
letterGrades = []

#Messy if/else
for person in range(len(students)):
    
    if math.floor(grades[person]) <= 100 and math.floor(grades[person]) > 92:
        letterGrades.append(' A ')
    
    elif math.floor(grades[person]) > 90 and math.floor(grades[person]) <= 92:
        letterGrades.append(' A- ') 
    
    elif math.floor(grades[person]) < 90 and math.floor(grades[person]) >= 87:
        letterGrades.append( ' B+ ')
    
    elif math.floor(grades[person]) < 87 and math.floor(grades[person]) >= 83:
        letterGrades.append( ' B ')
    
    elif math.floor(grades[person]) < 83 and math.floor(grades[person]) >= 80:
        letterGrades.append(' B- ')  
    
    elif math.floor(grades[person]) < 79 and math.floor(grades[person]) >= 77:
        letterGrades.append(' C+ ')     
    
    elif math.floor(grades[person]) < 77 and math.floor(grades[person]) >= 70:
        letterGrades.append(' C ') 
    
    elif math.floor(grades[person]) < 70 and math.floor(grades[person]) >= 60:
        letterGrades.append(' D ') 
    else:
        letterGrades.append(' F ')                       

#output

print("|" + "name".rjust(10) + "|".center(5) +"Grade".ljust(10) +"|" )
for person in range(len(students)):
    print("| " + students[person].rjust(10) + " | " + letterGrades[person].ljust(10) + " |")
   

#problem 3

foods =  ["Hoagie","sammie","Ropa veja", "ghoulash"] 


vowels = 'aeiouy'
output = "We will have a"
end = " at the party."
n = len(foods)

print(f"We have {n} foods!")

if foods[0][0] in vowels:
    output += 'n '    
else:
    output += ' '


if n ==1:
    output = foods[0] + '.'
elif n ==2:
    output += foods[0]+ ' and '+ foods[1] + '.'
else:
    for food in foods[:-1 ]:
        output += food + ', '
    output += 'and '+ foods[n-1] 
print(output + end)    

#next section of foods
output = 'We will have a '
foods = ["tuna melt","potato chips"]
n = len(foods)

print(f"We have {n} foods!")

if foods[0][0] in vowels:
    output += 'n '    
else:
    output += ' '


if n ==1:
    output = foods[0] + '.'
elif n ==2:
    output += foods[0]+ ' and '+ foods[1] + '.'
else:
    for food in foods[:-1 ]:
        output += food + ', '
    output += 'and '+ foods[n-1] 
print(output + end)  


#next section of foods
output = 'We will have a '
foods = ["salad"]
n = len(foods)

print(f"We have {n} foods!")

if foods[0][0] in vowels:
    output += 'n '    
else:
    output += ' '


if n ==1:
    output = foods[0] + '.'
elif n ==2:
    output += foods[0]+ ' and '+ foods[1] + '.'
else:
    for food in foods[:-1 ]:
        output += food + ', '
    output += 'and '+ foods[n-1] 
print(output + end)

#last section
foods = ["anchoive", "mustard", "olive oil"] 
# We will have an anchoive, mustard, and olive oil at the party. 
output = 'We will have a '

n = len(foods)

print(f"We have {n} foods!")

if foods[0][0] in vowels:
    output += 'n '    
else:
    output += ' '


if n ==1:
    output = foods[0] + '.'
elif n ==2:
    output += foods[0]+ ' and '+ foods[1] + '.'
else:
    for food in foods[:-1 ]:
        output += food + ', '
    output += 'and '+ foods[n-1] 
print(output + end)