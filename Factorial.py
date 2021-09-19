import math
Num = int(input('Enter number: '))

if Num < 0:
    print('Cannot get {}!'.format(Num))
    exit()
else:
    if Num  >=  0 :
        Y = math.factorial(Num)
        
print('{}! = {}'.format(Num,Y))
