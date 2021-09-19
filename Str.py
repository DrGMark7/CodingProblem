word = str(input('Enter text: '))
filt = str(input('Enter filter word: '))
n = len(filt)
print('Text after filter is','"'+word.replace(filt,'*'*n)+'"')