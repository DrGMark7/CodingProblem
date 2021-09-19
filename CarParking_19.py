# CarParking Central

Shopping = int(input("How much you Shopping ? : "))
Hour = int(input("Parking hours : "))
Minute = int(input("Minutes parked : "))

if (Shopping < 0) or (Hour < 0) or (Minute < 0):
    print("it can't be negative")
    exit()

# การคิดค่ารถเราจะแบ่งออกเป็น 2 กลุ่มใหญ่ คือลูกค้าที่ซื้อ 1000 บาทขึ้นไป
# กับไม่ถึง 1000 บาท

def CarParking():

    if Shopping >= 1000: # 1000 บาทขึ้นไป
        Cash_H_I = Hour*30 # สร้างตัวแปร 1 ตัว เพื่อคิดค่าใช้จ่ายโดยชั่วโมงอย่างเดียว             
        if Minute > 0: #= แบ่งเวลาออกเป็น 2 อย่างคือ มากกว่า 1 นาที 
            Value_I = 1 # ประกาศค่าคงตัว [ไม่ต้องทำก็ได้] ว่าถ้ามากกว่า 1 นาทีจะเท่ากับ 1 ชม. เสมอ 
            Cash_M_I = Value_I*30 # สร้างตัวแปรเก็บค่า จากค่าใช้จ่ายของเวลา เอาค่า Value คูณด้วย เรทราคาการคิดของชม. ที่จอดรถ            
        elif  Minute <= 0: #= หรือน้อยกว่า 1 นาที
            Value_II = 0 # ประกาศค่าคงตัว [ไม่ต้องทำก็ได้] ว่าถ้าน้อยกว่าเท่ากับ 0 นาทีจะเท่ากับ 0 ชม. เสมอ 
            Cash_M_I = Value_II*30 # ใช้ตัวแปรเดียวกันในการเก็บค่า แต่การใช้ If else แบบนี้จะติดสินเองว่าจะเอาอันไหนไปใช้เพราะ จะเลือกอันที่ถูกก่อนเสมอ
        # ในส่วนตรงนี้จะเป็นการสร้างค่าคงตัวของเวลาขึ้นมา 1 ตัว
        if Cash_M_I > 0 : # ถ้าค่าราคาของเวลาในหน่วยนาทีมีค่ามากกว่า 0 
            MinuteValue =  1 + (Cash_M_I - Cash_M_I) # จะให้ค่าคงตัวของเวลาเท่ากับ 1 เสมอเพราะ [เราจะนำไปคิดต่อในส่วนลด]
        elif Cash_M_I <= 0 : # ถ้าค่าราคาของเวลาในหน่วยนาทีมีค่าน้อยหว่าหรือเท่ากับ 0 
            MinuteValue =  0 + (Cash_M_I - Cash_M_I) # จะให้ค่าคงตัวของเวลาเท่ากับ 0 เสมอเพราะ [เราจะนำไปคิดต่อในส่วนลด]

        Cash_HM = Cash_H_I + Cash_M_I
        print(f'You parking fee {Cash_HM}')

        if Hour < 4:
            Cash_HM_I = Cash_HM - 30*(Hour+MinuteValue)
        elif Hour == 4:
            Cash_HM_I = Cash_HM - 30*Hour
        elif Hour > 4:
            Cash_HM_I = Cash_HM - 120
    elif Shopping < 1000:
        Cash_H_I = Hour*30
        if Minute > 0:
            Value_I = 1
            Cash_M_I = Value_I*30           
        elif  Minute <= 0:
            Value_II = 0
            Cash_M_I = Value_II*30      
             
        Cash_HM = Cash_H_I + Cash_M_I
        print(f'You parking fee {Cash_HM}')

        if Hour <= 1:
            Cash_HM_I = Cash_HM - 30
        elif Hour > 1:
            Cash_HM_I = Cash_HM - 30    

    if Cash_HM_I == 160:
        Cash = Cash_HM_I - 10
        print(f"Discount : {Cash_HM-Cash}")        
        print("Total Your parking fee {} ฿".format(Cash))
    elif Cash_HM_I <= 0:
        print(f"Discount : {Cash_HM-Cash}")        
        print("Total Your parking fee Free ฿")
    else:
        Cash = Cash_HM_I
        print(f"Discount : {Cash_HM-Cash}")
        print("Total Your parking fee {} ฿".format(Cash))  

CarParking()     
