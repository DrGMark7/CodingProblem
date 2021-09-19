import statistics

X = []
for Y in range(20):
    num = int(input('Enter number #'+str(Y+1)+': '))
    X.append(num)
   
F = list(dict.fromkeys(sorted(X)))
Z = str(F)

if '[' and ']' or ',' in Z :
    Z2 = Z.replace('[','')
    Z3 = Z2.replace(']','')
    Z4 = Z3.replace(',','')
    print('Unique numbers is', Z4)

B = set(F[::2])
G = float(statistics.mean(B))

print("Average number of even position in list is {:.2f}".format(G))