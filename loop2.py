x = int(input('Enter number: '))
n = bin(x)
nx = str(n)
dele = '0b'
nbx = nx.replace(dele,'')
print(x,'is '+nbx+' in base 2.')