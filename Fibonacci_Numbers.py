start = [1,1]

for i in range(8):
   start.append(start[i]+ start[i + 1] )
  
print(start)
