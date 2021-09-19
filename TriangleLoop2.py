A = int(input('Enter the number of rows: '))

for x in range(0,A):
  for y in range(A-x-1):
    print(" ",end="")
  for y in range(1,x+2):
    print('*',end="")
  print('')
