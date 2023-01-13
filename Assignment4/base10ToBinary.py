#Jacob Haber asked david for help
 
#base10 not method
# base10 = 500
# binary = [] 
# div = base10
# while div > 0:
#     rem = div % 2
#     binary.insert(0, rem)
#     div //= 2
# print(("".join(str(n) for n in binary)))

#base 10 as method
def  baseTenAsMethod(base10):
    binary = []
    div = base10
    while div > 0:
        rem = div % 2
        binary.insert(0,rem)
        div //= 2
    return "".join(str(n) for n in binary)
#expected output = 111110100
print(baseTenAsMethod(500))
