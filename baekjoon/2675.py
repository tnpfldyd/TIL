T = int(input())
for i in range(T):
    a, b = input().split()
    for j in b:
        print(j*int(a), end='')
    print()
