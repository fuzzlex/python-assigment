i = 0
plusagain = 0
number =  input("Enter a number please? ")
while not number.isdigit():
  print("Your format is incorrect")
  number = input("Enter a number please? ")
a = list(number)
while i < len(a) :
  x = int(a[i]) ** len(a) 
  plusagain = plusagain + x
  
  i += 1
if plusagain == int(number) :
  print(number, " is an Armstrong number")
else:
  print(number, " isn't an Armstrong number")
