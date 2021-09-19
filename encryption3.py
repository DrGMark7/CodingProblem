Word = str(input('Enter 5 characters: '))
Word_N = Word.lower()

import string
S_Word = string.ascii_lowercase *2

NW = " "
for a in Word_N :
    if a in Word_N :
        NW= NW + S_Word[S_Word.find(a)+(-13)]
    elif a in Word_N :
        NW = NW + S_Word[S_Word.find(a)+(-13)]

print ('Encryption is',NW )

