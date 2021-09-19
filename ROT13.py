print('Select 2 options' + '\n'+' - 1 encrypt with ROT 13'+'\n'+' - 2 decrypt with ROT 13')
print('')
C = str(input('Choose option: '))
import string

R13 = input('Enter text: ')
B_Word = string.ascii_uppercase *945811
S_Word = string.ascii_lowercase *324730

R_13 = ''
if '1' in C :
    for a in R13 :
        if a in B_Word :
            R_13 = R_13 + B_Word[B_Word.find(a)+13]
        elif a in S_Word :
            R_13 = R_13 + S_Word[S_Word.find(a)+13]
        else :
            R_13 = R_13 + a
        
    print('Ciphertext is "{}"'.format(R_13))

if '2' in C :
    for a in R13 :
        if a in B_Word :
            R_13 = R_13 + B_Word[B_Word.find(a)-13]
        elif a in S_Word :
            R_13 = R_13 + S_Word[S_Word.find(a)-13]
        else :
            R_13 = R_13 + a
    print('Plaintext is "{}"'.format(R_13))
