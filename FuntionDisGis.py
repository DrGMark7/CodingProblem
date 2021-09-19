product = input('Enter product type: ')
price = float(input('Enter price: '))
def discount():
    if 'food' in product:
        return'Price after discount is ' + '{:.2f}'.format((price*97)/100)
    if 'medicine' in product:
        return'Price after discount is ' + '{:.2f}'.format((price*99)/100)
    if 'shoes' in product:
        return'Price after discount is ' + '{:.2f}'.format((price*80)/100)
    if 'shoes' not in product and 'medicine' not in product and 'food' not in product:
        return 'Price after discount is ' + '{:.2f}'.format(price)
print(discount())