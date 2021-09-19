Gender = input('Enter Gender (M/W): ')
if Gender != 'M' and Gender != 'W':
    print( Gender,'is not M or W')
    exit()
CYears =int(input('Enter current year: '))
BYears =int(input('Enter your birth year: '))
W =float(input('Enter your weight (kg): '))
H =float(input('Enter your height (cm): '))
Age = CYears - BYears
Hm = H/100
BMI = W/(Hm**2)
print('- '*6)
print('Your age =',Age)
print('Your BMI =',round(BMI,3))
if Gender == 'M' :
    BMR = 66.5 + (13.75 * W) + (5.003 * H) - (6.755 * Age)
    print('Your BMR =','{:.3f}'.format(BMR))
if Gender == 'W' :
    BMR = 655.1 + (9.563 *W) + (1.850 * H) - (4.676 * Age)
    print('Your BMR =','{:.3f}'.format(BMR))    