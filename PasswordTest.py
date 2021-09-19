"""Strong Password"""
def main():
    def Password_Safe(Pwd):

        Pwd = str(Pwd)
        Pwd_L = list(Pwd)

        L_Digit = []
        L_Alpha = []
        L_Upper = []
        L_Lower = []
        
        for i in Pwd_L:
            # Digit
            if i.isdigit() == True:
                L_Digit.append(1)
            else :
                L_Digit.append(0)

            #Alpha 
            if i.isalpha() == True:
                L_Alpha.append(1)
            else:
                L_Alpha.append(0)

            # Upper
            if i.isupper() == True:
                L_Upper.append(1)
            else :
                L_Upper.append(0)

            # Lower   
            if i.islower() == True:
                L_Lower.append(1)
            else :
                L_Lower.append(0)

        def islenmore_10(Pwd):

            if len(Pwd) > 10:
                Count = len(Pwd[9:len(Pwd)-1])
            else :
                Count = 0
            
            return Count

        def PwdAGAIN(Pwd):

            Pwd_L = list(Pwd)
            List_P = sorted(list(set(Pwd_L)),reverse=False)
            List = []
            Conut_Pass = []
            for i in List_P:
                if i in List:
                    (set(Pwd_L)).remove(i)
                    
                Conut_Pass.append(Pwd_L.count(i))
                List.append(i) 

            LenFirst = Conut_Pass[0]
            if LenFirst > 4:
                dis = 15*(LenFirst-4)
            else :
                dis = 0
        
            return dis

        Z_Alpha = sum(L_Alpha)
        Z_Digit = sum(L_Digit)    
        Z_Upper = sum(L_Upper)
        Z_Lower = sum(L_Lower)

        Count = islenmore_10(Pwd)
        Dis = PwdAGAIN(Pwd)

        Plus = Count*10
        FDis = Dis*15
        Last = ord(Pwd[-1])

        if Z_Alpha == len(Pwd):
            Score_2 = 30
        else:
            Score_2 = 0

        if Z_Digit == len(Pwd):
            Score = 50
        elif (Z_Lower + Z_Upper) == len(Pwd):
            Score = 175
        elif (Z_Alpha + Z_Digit) == len(Pwd):
            Score = 75      
        elif Z_Lower == len(Pwd):
            Score = 100
        elif Z_Upper == len(Pwd):
            Score = 85
        
        
        Final = ((Score+Plus) - FDis) + Last + Score_2

        if Final < 150 :
            Security = 'poor'
        elif Final < 300:
            Security = 'acceptable'
        elif Final >= 300 :
            Security = 'secure'

        # print(f'Z_Alpha : {Z_Alpha}')
        # print(f'Z_Digit : {Z_Digit}')
        # print(f'Z_Upper : {Z_Upper}')
        # print(f'Z_Lower : {Z_Lower}')
        # print(f'Plus : {Plus}')
        # print(f'FDis : {FDis}')
        # print(f'Last : {Last}')
        # print(f'Score : {Score}')

        print('Password : {}'.format('*'*(len(Pwd))))
        print(f'Security score : {Final}')
        print(f'Security level : {Security}')

        return Final

    Password_List = []
    Time = []

    while True:

        Password = str(input())
        
        if (sum(Time) == 0) and len(Password) < 6:
            print('try again')        
        elif sum(Time) == 0:
            Password_Safe(Password)

        if (sum(Time) >= 1) and (len(Password) < 6):
            print('process terminated')
        elif sum(Time) >= 1:
            Password_Safe(Password)

        Time.append(1)

        if sum(Time) == 2:
            break
main()    
    




        

