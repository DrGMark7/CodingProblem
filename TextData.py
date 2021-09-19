File = open("C:\\Users\\User\\Pictures\\Chokun\\Python\\Python Basic Logic\\Datatest.txt" , mode='r' , encoding='utf-8')

a = ''
List_Text = []

while '' in a:
    a = str(input('Enter Text : '))

    if 'end' in a:
        break    
    List_Text.append(a)

Text = ''.join(List_Text)




