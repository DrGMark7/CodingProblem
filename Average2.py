l1 = []
for i1 in range(20):
    num = int(input('Enter number #'+str(i1+1)+': '))
    l1.append(num)
s1 = set(l1)
uni = ''
for i in s1:
    uni += str(i)+' '
print('Unique numbers is {}' .format(uni[:-1]))
l1 = list(s1)
l2 = []
for i2 in l1[::2]:
    l2.append(i2)
print('Average number of even position in list is {:.2f}' .format(sum(l2)/len(l2)))