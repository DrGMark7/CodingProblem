Nums = []
Num = 0

while Num >= 0 :
    Num = int(input('Enter number: '))
    if Num < 0 :
        break
    Nums.append(Num)

Nums.sort()
print("Minimum number is", Nums[0])
print("Maximum number is", Nums[-1])


