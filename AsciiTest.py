import string

S_Word = string.ascii_lowercase
B_Word = string.ascii_uppercase
Dig = string.digits

N = str(input('Enter Number : '))
Ascii = ""
for a in N :

    if a in B_Word :
        Ascii = Ascii + B_Word[B_Word.find(a)+13]
    elif a in S_Word :
        Ascii = Ascii + B_Word[S_Word.find(a)+13]

print(Ascii)