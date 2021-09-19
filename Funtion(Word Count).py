T = ''
TE = []

while T != 'end' :
    T = input('Enter text: ')
    if T != 'end' :
        TE.append(T)

def word_count():
    x = 0
    for l in TE:
        x += 1 + l.count(' ')
    return x

Y = str(word_count()) 

print('Got {} words'.format(Y))