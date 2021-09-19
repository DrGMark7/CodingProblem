A = int(input('Enter the number of rows: '))
S = str(input('Enter print symbol: '))

for x in range(A,0,-1):
  for y in range(A - x):
    print (" ",end="")
  for y in range(1,x + 1):
    print(S,end="")
  for y in range(2,x + 1):
    print(S,end="")  
  print()