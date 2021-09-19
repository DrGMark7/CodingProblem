T = ''
TE = []
while '' in T :
    T = str(input('Enter string: ')).lower()
    if 'end' in T : 
        break
    TE.append(T)
TA = ''.join(TE)

print('*'*30)
print('*     Alphabet Counting      *')
print('*'*30)

C = "abcdefghijklmnopqrstuvwxyz"

for char in C :
  count = TA.count(char)
  if count > 0:
    print(char, count)

print('*'*30)




