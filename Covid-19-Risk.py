co1, co2, co3 = 0,0,0 
age = input("Are you a cigarette addict older than 75 years old? ") .capitalize().strip()
chronic = input("Do you have a severe chronic disease? " ).capitalize().strip()
immune = input("Is your immune system too weak? ").capitalize().strip()
for i in age,chronic,immune :
   if age == "Yes" :
    co1 = 1
   elif chronic == "Yes" :
    co2 = 1
   elif immune == "Yes" :
    co3 = 1
   else:
    print("Your answer is invalid")
    break
if (co1 == 0 and co2 == 0) and co3 == 0 :
  print("You havent any  dealth risk")
else :
  print("You have a dealth risk")
