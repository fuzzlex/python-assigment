com = 0
num = int(input("Enter a number please? "))
for i in range(2,num) :
    if (num % i) == 0 :
      com = 1

if com == 0  :
  print(num, "is a Prime Number")
else :
    print(num, "isn't a prime number")
