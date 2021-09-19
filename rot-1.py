charc = input('Enter 3 characters: ')
UpperWord = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
LowerWord = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
rot_1 = ""
for c in charc :
    if c in UpperWord :
        rot_1 = rot_1 + UpperWord[UpperWord.find(c)+1]
    elif c in LowerWord :
        rot_1 = rot_1 + UpperWord[LowerWord.find(c)+1]

print('Ciphertext is',rot_1)