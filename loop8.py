n = int(input('Enter the number of rows: '))*2
sym = input('Enter print symbol: ')
for i in range(n-1,0,-2):
	print(' '*(((n-i)//2))+sym*i)