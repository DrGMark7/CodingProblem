num = int(input("Enter the number of rows: "))
for i in range(num,0,-1):
    for j in range(num-i,0,-1):
        print(end=" ")
    for j in range(i,0,-1):
        print("*",end="")
    print()