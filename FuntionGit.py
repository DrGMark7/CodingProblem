l1 = []
text = ''
while text != 'end':
    text = input('Enter text: ')
    if text != 'end':
        l1.append(text)

def word_count():
    wcount = 0
    for i in l1:
        wcount += 1+i.count(' ')
    return wcount
    
print('Got', word_count() ,'words')