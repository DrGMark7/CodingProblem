G = str(input('Enter Gender (M/W): '))

if G != 'M' and G != 'W' :
    print(G,"is not M or W")
    exit()

Y2 = int(input('Enter current year: '))
Y = int(input('Enter your birth year: '))
W = float(input('Enter your weight (kg): '))
H = float(input('Enter your height (cm): '))

print('- '*6)

ΔY = Y2 - Y 
print('Your age =', ΔY)

HM = H/100 
BMI = W/(HM)**2
print('Your BMI =',round(BMI,3))

if "M" in G : 
    BMR_M = 66.5 + (13.75*W) + (5.003*H) - (6.755*ΔY)
    print('Your BMR =','{:.3f}'.format(BMR_M))

if "W" in G :
    BMR_W = 655.1 + (9.563*W) + (1.850*H) - (4.676*ΔY)
    print('Your BMR =','{:.3f}'.format(BMR_W))
