def s_couter() :
  k = {}
  a = input("Enter a sentence please?  ").lower()
  b = list(a)
  c = set(b)
  for i in c :
    k[i] = b.count(i)
  return k
s_couter()
