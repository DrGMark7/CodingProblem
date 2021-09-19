T = ''
TE = []
while '' in T :
    T = str(input('Enter string: ')).lower()
    if 'end' in T : 
        break
    TE.append(T)
TA = str(TE)

if '[' and ']' or ',' or "'" or "\\" or '’' or '!' or '-' or '>' or '/' in TA :
    A = TA.replace('[','')
    B = A.replace(']','')
    C = B.replace(',','')
    D = C.replace("'",'')
    E = D.replace('\\','')
    F = E.replace('!','')
    G = F.replace('’','')
    H = G.replace('-','')
    I = H.replace('>','')
    J = I.replace('/','')

print('*'*30)
print('*     Alphabet Counting      *')
print('*'*30)
   
def count_repeated_letter(string1):
    list1=[]

    for letter in string1:
        if string1.count(letter)>= 1:
            if letter not in list1:
                list1.append(letter)


    for item in list1:
        if item!= " ":
            print(item,string1.count(item))

count_repeated_letter(J)

print('*'*30)