num = int(input('Enter number: '))
factorial = 1
numx = str(num) +'!'
if num < 0:
   print('Cannot get '+numx)
elif num == 0:
   print(numx,"=",1)
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print(numx,"=",factorial)
