print('*'*30 + '\n' +'*'*9 + 'About Circle' +'*'*9 + '\n' + '*'*30 )
import math
radius = float(input('Input radius: '))
print('Radius is', radius)
Circumference = ((2*math.pi)*radius)
print('Circumference is {:.4f}'.format(Circumference))
Area = (math.pi)*(radius**2)
print('Area is {:.2f}'.format(Area))
y = float(input('Enter y for finding x: '))
print('y is {:.4f}'.format(y))
x = math.sqrt((radius**2)-(y**2))
print('x is -{:.4f}'.format(x) ,'and' ,'{:.4f}'.format(x)) 
print('******************************')