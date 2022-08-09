T = input()
while True:
    cnt = 0
    T = str(T)
    for i in T:
        if i == '7' or i == '4':
            cnt += 1
    
    if len(T) == cnt:
        print(T)
        break
    else:
        T = int(T) - 1
