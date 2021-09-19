num = (input('Enter value in mm, cm, and m: '))
convert = (input('Enter unit to convert in mm, cm, m: '))

if 'cm' in num :
    num2 = float(num[:-2])
    if 'mm' in convert :
        print('Value after unit conversion is','{}'.format(num2*10)+'mm')
    elif 'm' in convert :
        print('Value after unit conversion is','{}'.format(num2/100)+'m')
    else :
        print('Value after unit conversion is','{}'.format(num2)+'cm')
    exit()

if 'mm' in num :
    num3 = float(num[:-2])
    if 'cm' in convert :
        print('Value after unit conversion is','{}'.format(num3/10)+'cm')
    elif 'm' in convert :
        print('Value after unit conversion is','{}'.format(num3/1000)+'m')
    else :
        print('Value after unit conversion is','{}'.format(num3)+'mm')
    exit()

if 'm' in num :
    num4 = float(num[:-1])
    if 'cm' in convert :
        print('Value after unit conversion is','{}'.format(num4*100)+'cm')
    elif 'mm' in convert  :
        print('Value after unit conversion is','{}'.format(num4*1000)+'mm')
    else :
        print('Value after unit conversion is','{}'.format(num4)+'m')
    exit()