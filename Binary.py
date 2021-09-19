Decimal = int(input('Enter number: '))
Binary = bin(Decimal)
N_Binary = Binary[2:]
print('{} is {} in base 2.'.format(Decimal,N_Binary))