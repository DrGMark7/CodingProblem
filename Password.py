def Pass_Safety(Pwd):    
    Pwd = str(Pwd)
    Pwd_L = list(Pwd)

    L_Len = []
    def islen(Pwd):    
        if (len(Pwd) > 6) and (len(Pwd) < 12):
            L_Len.append(1)
        else:
            L_Len.append(0)
    islen(Pwd)
    
    def isspecial(i):
        List = []

        if i == '#':
            List.append(1)
        elif i == '$':
            List.append(1)
        elif i == '@':
            List.append(1)
        else:
            List.append(0)

        Zigma = sum(List)
        if Zigma >= 1:
            A = 1
        else :
            A = 0

        return bool(A)

    L_lower = []
    L_Upper = []
    L_digit = []
    L_Special = []
    L_Space = []
    for i in Pwd_L:
        # Lower
        if i.islower() == True:
            L_lower.append(1)
        else :
            L_lower.append(0)

        # Upper
        if i.isupper() == True:
            L_Upper.append(1)
        else :
            L_Upper.append(0)

        # Digit
        if i.isdigit() == True:
            L_digit.append(1)
        else :
            L_digit.append(0)

        # Special
        if isspecial(i) == True:
            L_Special.append(1)
        else:
            L_Special.append(0)
        
        # Space 
        if i.isspace() == True:
            L_Space.append(1)
        else:
            L_Space.append(0)

    Z_lower = sum(L_lower)
    Z_Upper = sum(L_Upper)
    Z_digit = sum(L_digit)
    Z_Special = sum(L_Special)
    Z_Space = sum(L_Space)
    Z_Len = sum(L_Len)

    if (Z_lower >= 1) and (Z_Upper >= 1) and (Z_digit >= 1) and (Z_Special >= 1) and (Z_Space == 0) and (Z_Len == 1):
        A = bool(1)
    else :
        A = bool(0)

    return A

# A = str(input())
# B = str(input())
# C = str(input())

# Password = str(input())
# List_P = Password.split(',')
# List_M = [A,B,C]

# NList_P = []
# for i,j in zip(List_P,List_M):
#     if Pass_Safety(i) == True:
#         NList_P.append(i)        
#         print(f'{i} ({j})')
    

    

