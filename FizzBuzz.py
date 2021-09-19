Num = int(input('Enter number: '))
print('The number is', Num)

if (Num %3) == 0 and (Num %5) == 0 :
    print('FizzBuzz')

if (Num %5) == 0 and (Num%3) != 0:
    print('Buzz')    
    
if (Num %3) == 0 and (Num%5) != 0:
    print('Fizz') 