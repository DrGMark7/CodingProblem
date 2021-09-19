"""Car Park"""
def main():
    def CarPark(Dayf,Timef,Dayl,Timel):

        # เช็ค Error Parameter

        # การแปลงเวลาในระบบเลขฐานสิบ
        # สมมติให้ จำนวนเต็ม 100 ประกอบขึ้น จาก  1 เพียง 100ตัว
        # ใน         1 ชม     ประกอบขึ้น จาก  1 นาที 60 ตัว
        # แสดงว่า ถ้าเราขยาย Range ของเวลาให้อยู่ในรูปเลข 1 นาทีจะมีค่า 1/60
        # ในมุมมองเดียวกัน 1 วัน มี 24 ชม.
        #  แสดงว่าในหน่วยคณิตศาสตร์ 1 ชม. จะมีค่า 1/24 จึงสามารถตั้งเป็นค่าคณิตศาสตร์ได้
        # 1Day = 24H  --->  1H = 1/24Day
        
        DTimef = ((Dayf*24) + (Timef))/24
        DTimel = ((Dayl*24) + (Timel))/24
        DeltaTime  = DTimel - DTimef

        Hour = (DeltaTime % 1)*24
        Day = DeltaTime//1
        
        # การคิดราคา 
        if (Day < 1) and (Hour < 3):
            Price = 0
        elif (Day < 1) and (Hour > 2) and (Hour < 13):
            Price = 15*Hour
        elif (Day > 0) and (Hour >= 0) and (Hour <= 12):
            Price = 200*Day + (Hour*15)
        elif (Day > 0) and (Hour > 12) and (Hour < 24):
            Price = 200*(Day+1)

        #การคิดส่วนลด
        Week = Day // 7
        if (Week >= 1) and (Week < 4):
            Discount = 300*Week
        elif (Week >= 4):
            Discount = (300*Week) + 500
        else:
            Discount = 0

        #คิดราคาสำเร็จ
        Final = Price - Discount
        if Final < 0 :
            Final = 0
        else : 
            Final = Final

        return int(Final)
        

    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    if A > C:
        print('error')
    elif (A > 365) or (B > 24) or (C > 365) or (D > 24) :
        print('error')
    elif (A <= 0) or (B < 0) or (C <= 0) or (D < 0):
        print('error')
    elif (A == B == C == D):
        print('error')          
    else:
        DTimef = ((A*24) + (B))/24
        DTimel = ((C*24) + (D))/24
        DeltaTime  = DTimel - DTimef
        Hour = int((DeltaTime % 1)*24)
        Day = int(DeltaTime//1)
        Finish = int(CarPark(A,B,C,D))
        print('%d day %d hour'%(Day,Hour))
        print('%d baht'%(Finish))
main()

