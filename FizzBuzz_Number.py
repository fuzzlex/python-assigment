def number(a) :
  number_list = list(range(100))
  for a in number_list :
   if a == 0 :
    print("")
   elif a in number_list[::15] :
    print("Fizzbuzz" , sep="-")
   elif a in number_list[::3] :
    print("Fizz", sep="-")
   elif a in number_list[::5] :
    print("Buzz", sep="-")
   elif a in number_list[::1] :
    print(a, sep="-")
  
number(a)
