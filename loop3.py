size = int(input('Enter the number of rows: '))
for row in range (1,size + 1):
    for col in range (1,row + 1):
        print("*", end="")
    print()