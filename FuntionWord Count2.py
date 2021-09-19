l1 = []
text = ''
while text != 'end':
    text = input('Enter text: ')
    if text != 'end':
        l1.append(text)
word_count = 0
for i in l1:
    count = 0
    for i2 in i:
        if ' ' in i2:
            count += 1
    count += 1
    word_count += count 
print('Got {} words' .format(word_count))