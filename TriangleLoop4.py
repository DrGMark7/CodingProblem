Num = int(input('Enter the number of rows: '))
for x in range(Num,0,-1):
  for y in range(Num-x,0,-1):
    print (end=" ")
  for y in range(x,0,-1):
    print('*',end="")
  print()