T = int(input())
for i in range(T):
    if i%2 != 0 :
        print(' ',end='')
    for j in range(T):
        print('*',end=' ')
    print()