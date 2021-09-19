# CarParking Central

Shopping = int(input("How much you Shopping ? : "))
Hour = int(input("Parking hours : "))
Minute = int(input("Minutes parked : "))

def CarParking():

    if Shopping >= 1000:
        Cash_H_I = Hour*40              
        if Minute > 0:
            Value_I = 1
            Cash_M_I = Value_I*40            
        elif  Minute <= 0:
            Value_II = 0
            Cash_M_I = Value_II*40
        
        if Cash_M_I > 0 :
            MinuteValue =  1 + (Cash_M_I - Cash_M_I)
        elif Cash_M_I <= 0 :
            MinuteValue =  0 + (Cash_M_I - Cash_M_I)

        Cash_HM = Cash_H_I + Cash_M_I

        if Hour <= 3:
            Cash_HM_I = Cash_HM - 40*(Hour+MinuteValue)
        elif Hour > 3:
            Cash_HM_I = Cash_HM - 120
    elif Shopping < 1000:
        Cash_H_I = Hour*40
        if Minute > 0:
            Value_I = 1
            Cash_M_I = Value_I*40           
        elif  Minute <= 0:
            Value_II = 0
            Cash_M_I = Value_II*40      
             
        Cash_HM = Cash_H_I + Cash_M_I

        if Hour <= 1:
            Cash_HM_I = Cash_HM - 40
        elif Hour > 1:
            Cash_HM_I = Cash_HM - 40

    if Cash_HM_I == 160:
        Cash = Cash_HM_I - 10
        print("Your parking fee {} ฿".format(Cash))
    elif Cash_HM_I <= 0:        
        print("Your parking fee Free ฿")
    else:
        Cash = Cash_HM_I
        print("Your parking fee {} ฿".format(Cash))  

CarParking()     
