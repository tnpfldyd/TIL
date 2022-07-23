import sys

sys.stdin = open("1946input.txt", "r")

T = int(input())

for i in range(1, T+1):
    print('#'+str(i))
    a = int(input())
    R = ''
    for j in range(a):
        b, c = input().split()
        c = int(c)
        R += b * c
    for k in range(len(R)):
        if (k+1) % 10 == 0:
            print(R[k])
        else:
            print(R[k], end='')
    print()