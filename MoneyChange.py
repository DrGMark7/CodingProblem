Money = float(input('Enter You Money : '))
Price = float(input('Enter You Price for Product : '))
MoneyC = abs(Money - Price)
print(f'Your withdrawal {MoneyC} Thai Bath')
if MoneyC > 0:
    #500 Bath
    B500 = MoneyC//500    
    A500 = MoneyC-(500*B500)    
    #100 Bath
    B100 = A500//100    
    A100 = A500-(100*B100)
    #50Bath
    B50 = A100//50  
    A50 = A100-(50*B50)
    #20 Bath
    B20 = A50//20
    A20 = A50-(20*B20)
    #10 Bath
    B10 = A20//10
    A10 = A20-(10*B10)
    #5 Bath
    B5 = A10//5
    A5 = A10-(5*B5)
    #1 Bath
    B1 = A5//1
    A1 = A5-(1*B1)
    #0.5 Bath
    B0_5 = A1//0.5
    A0_5 = A1-(0.5*B0_5)
    #0.25 Bath
    B0_25 = A0_5//0.25
    A0_25 = A0_5-(0.25*B0_25) 

    print(f'500 Bath    [{int(B500)}] ใบ')
    print(f'100 Bath    [{int(B100)}] ใบ')
    print(f'50 Bath     [{int(B50)}] ใบ')
    print(f'20 Bath     [{int(B20)}] ใบ')
    print(f'10 Bath     [{int(B10)}] เหรียญ')
    print(f'5 Bath      [{int(B5)}] เหรียญ')
    print(f'1 Bath      [{int(B1)}] เหรียญ')
    print(f'50 Satang   [{int(B0_5)}] เหรียญ')
    print(f'25 Satang   [{int(B0_25)}] เหรียญ')
    ########################################   
elif MoneyC == 0:
    print('Get the money just right.')
else:
    exit()