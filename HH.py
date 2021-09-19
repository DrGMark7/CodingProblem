T = ''
TE = []

while '' in T :
    T = str(input('Enter string: ')).lower()
    if 'end' in T :
        break
    TE.append(T)    

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency(TE))