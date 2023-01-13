#Jacob Haber asked david shin for help
#d for dictionary
d = {
  "1": "9",
  "2": "8",
  "3": "7",
  "4": "6",
  "5": "0",
  "9": "1",
  "8": "2",
  "7": "3",
  "6": "4",
  "0": "5"

}

def obfuscated(phone_numbers):
  #store string
  convert = ""
  #loops through string 
  for num in phone_numbers:
    if num in d:
      convert += d[num]
    else:
      convert += num
  return convert    

#phoneNumbers
phone_numbers = ['1-800-223-6283', 
                  '555-1234', 
                  "Jenny's phone number is 867-5309"] 
#DEFINE YOUR DICTIONARY AND ANY OTHER VARIABLES THAT ARE CONSTANT HERE 
for pn in phone_numbers: 
  print(obfuscated(pn)) 
  # Write your translation code here 