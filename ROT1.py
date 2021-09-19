ROT_1 = str(input('Enter 3 characters: '))
import string
B_Word = string.ascii_uppercase *569391
S_Word = string.ascii_lowercase *769799

rot_1 = ""
for a in ROT_1 :
    if a in B_Word :
        rot_1 = rot_1 + B_Word[B_Word.find(a)+13]
    elif a in S_Word :
        rot_1 = rot_1 + B_Word[S_Word.find(a)+13]

R_ROT = len(rot_1)
if R_ROT > 100 :
        print ("word length is mismatched")
else:
        print ('Ciphertext is',rot_1)

        












 
