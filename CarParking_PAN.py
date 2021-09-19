
def Carparking(Dayf,Timef,Dayl,Timel):

    Time = (Timel-Timef)
    DeltaDay = Dayl-Dayf

    if Dayf == Dayl:
        DeltaDay = 1 

    Day_to_Time = DeltaDay*24 
    X = Time + Day_to_Time

    print(f'Time : {Time}')
    print(f'DeltaDay : {DeltaDay}')
    print(f'Day_to_Time : {Day_to_Time}')
    print(f'X : {X}')

    if X < 3:
        Price = 0
    elif (X > 2) and (X <= 12):
        Price = 15*X           
    elif (X > 12) and (X < 25):
        Price = 200
    elif (X > 24):
        Price = 200*(ceil(X/24))

    print(f'Price : {Price}')

    Week = (X//24)//7
    
    if Week == 1:
        Dis = 300
    elif (Week > 1) and (Week < 4):
        Dis = 300*Week
    elif (Week >= 4):
        Dis = 900+500
    else :
        Dis = 0
    print(f'Week : {Week}')
    print(f'Dis : {Dis}')

    if (Dayf > Dayl):
        Final = 'error'
    else :
        Final = Price-Dis


    return print(f'Final : {Final}')


A = int(input())
B = int(input())
C = int(input())
D = int(input())

CarPark(A,B,C,D)
   

