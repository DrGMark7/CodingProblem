A = ''
N = int(input())
for i in range(N):
    if command=="insert":
        L.insert(i,e)
    elif command=="remove":
        L.remove(e)
    elif command=="append":
        L.append(e)
    elif command=="sort":
        L.sort()
    elif command=="pop":
        L.pop()
    elif command=="reverse":
        L.reverse()
    elif command=="print":
        print(L)