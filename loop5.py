row= int(input("Enter the number of rows: "))
k=row+1
for i in range(1,row+1): 
    for j in range(1,k):
        print("*", end="")
    k=k-1
    print()