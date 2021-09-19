def pro_1(n,X,dis):
    if n >= 3:
        Price = X*((100-dis)/100)
    return Price*n

def pro_2(n,X):
    N = n - (n // 4)
    Price = X*N #N คือ จำนวนคนหลังการลดโปรโมชั่น 4 จ่าย 3
    return Price

N = int(input())
X = int(input())
dis = int(input())

if (pro_1(N,X,dis) > pro_2(N,X)):
    Final_P = pro_2(N,X)
    Typ_Pro = 2
else :
    Final_P = pro_1(N,X,dis)
    Typ_Pro = 1

print('Promotion {} {:.3f} Bath'.format(Typ_Pro,Final_P))
print('Purchase successfully !')
print('Have a good meal with "Kanomwhan"')