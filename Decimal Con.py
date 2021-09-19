BI = int(input('Enter Number: '))

base2 = " "
IT = BI

while IT > 0 : 

    frac = int(IT//2)
    base2 = str(frac) + base2
    IT = (IT-frac) /2

print('{} is {} in base 2.'.format(BI,IT))