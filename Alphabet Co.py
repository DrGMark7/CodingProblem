import string

text = ''
text2 = ''

while text != 'end':
    text = input('Enter string: ').lower()
    if text != 'end':
        text2 += text
l1 = []
for i1 in text2:
    if i1 in string.ascii_lowercase:
        l1.append(i1) 

print('*'*30)
print('' + ' '*5 + 'Alphabet Counting' + ' '*6 + '')
print('*'*30)

l2 = l1.copy()[::-1]
for i in l2:
    while l2.count(i) > 1:
        l2.remove(i)

l2 = l2[::-1]
d1 = dict()
for i in l2:
    d1[i] = l1.count(i)
    
for i in d1:
    print('{} {}'.format(i, d1[i]))
print('*'*30)



