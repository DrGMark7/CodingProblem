Cargo = str(input('Enter product type: ')) 
Price = float(input('Enter price: '))

def discount() :
    if 'food' in Cargo :
        N = Price-(Price*0.03)
    elif 'shoes' in Cargo :
        N = Price-(Price*0.2)
    elif 'medicine' in Cargo :
        N = Price-(Price*0.01)
    else:
        N = Price

    return N

B = float(discount())
print('Price after discount is {:.2f}'.format(B))   