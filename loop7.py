n = int(input('Enter the number of rows: '))*2
system = input('Enter print symbol: ')
for i in range(1,n+1,2):
	print(' '*(((n-i)//2))+system*i)