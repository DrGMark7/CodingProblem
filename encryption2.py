import string
Word = str(input('Enter 5 characters: ')).lower()

SmallWord = string.ascii_lowercase *2
RSWord = SmallWord[::-1]

RPDict = dict(zip(SmallWord, RSWord))
RSDict = ''.join(map(RPDict.get, Word))

print('Encryption is', RSDict,)