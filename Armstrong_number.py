i = 0
plusagain = 0
number =  input("Hackendiinzi? ")
a = list(number)
while i < len(a) :
  x = int(a[i]) ** len(a) 
  plusagain = plusagain + x
  i += 1
if plusagain == int(number) :
  print(number, " is an Armstrong number")
else:
  print(number, " isn't an Armstrong number") 
