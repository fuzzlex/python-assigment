number_list = list(range(100))
for a in number_list :
  if a == 0 :
    print("")
  elif a in number_list[::15] :
    print("Fizzbuzz")
  elif a in number_list[::3] :
    print("Fizz")
  elif a in number_list[::5] :
    print("Buzz")
  elif a in number_list :
    print(a)
  
