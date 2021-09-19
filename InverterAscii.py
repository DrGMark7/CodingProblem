# Inverter Ascii
# https://th.wikipedia.org/wiki/%E0%B9%81%E0%B8%AD%E0%B8%AA%E0%B8%81%E0%B8%B5

print('Inverter Ascii')
print('2 base Number : [2]')
print('10 base Number : [10]')
print('str Text : [A]')

print('From')
Choice = str(input('Choose My Choice : '))
print('To')
Choice2 = str(input('Choose My Choice : '))

import string

def Decinmal_Bi():
    
    Binary = bin(Dec_Bi)
    N_Binary = Binary[2:]

    return N_Binary

def Binary_Dec():
    
    Decimal = 0
    for digit in Bi_Dec :
        Decimal = Decimal*2 + int(digit)
    
    return Decimal

def Ascii_Inv():
    Ascii = chr(Binary_Dec())
    print(Ascii)
    return Ascii

if ('2' in Choice ) and ('10' in Choice2):
    
    Bi_Dec = input('Enter Binary Number To Change : ')
    
    print('{} is {} in Number Base 2 '.format(Bi_Dec,Binary_Dec()))

if ('10' in Choice) and ('2' in Choice2):

    Dec_Bi = int(input('Enter Deciaml Number To Change : '))

    print('{} is {} in Number Base 10'.format(Dec_Bi,Decinmal_Bi()))

if ('2' in Choice) and ('A' in Choice2):

    Bi_Dec = input('Enter Binary Number To Change : ')

    A = Binary_Dec()

    print('{} is {} in Ascii Code'.format(Bi_Dec,(chr(A))))

if ('10' in Choice) and ('A' in Choice2):

    Dec_Bi = int(input('Enter Deciaml Number To Change : '))

    print('{} is {} in Ascii Code'.format(Dec_Bi,(chr(Dec_Bi))))

if ('A' in Choice) and ('10' in Choice2):

    Alpha = str(input('Enter Alphabet To Change : '))

    print('{} is {} in Number Base 10'.format(Alpha,(ord(Alpha))))

if ('A' in Choice) and ('2' in Choice2):

    Alpha = str(input('Enter Alphabet To Change : '))

    Dec_Bi = ord(Alpha)    

    print('{} is {} in Number Base 2'.format(Alpha,Decinmal_Bi()))   
        
