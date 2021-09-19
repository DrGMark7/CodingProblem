import string
InWord = str(input('Enter text: '))
OutWord = str(input('Enter filter word: '))
InOut = len(OutWord)
print('Text after filter is','"' +InWord.replace(OutWord,'*'*InOut) + '"')

