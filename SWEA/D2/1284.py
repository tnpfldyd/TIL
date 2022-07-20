import sys

sys.stdin = open("1284input.txt", "r")


T = int(input())

for i in range(1, T+1):
    a = list(map(int, input().split()))
    b = a[0]*a[4]
    c = a[1:5]
    if c[1] > c[3]:
        if b < c[0]:
            print('#'+str(i), b)
        else:
            print('#'+str(i), c[0])
    else:
        if b > c[0] + ((c[3]-c[1]) * c[2]):
            print('#'+str(i), c[0] + ((c[3]-c[1]) * c[2]))
        else:
            print('#'+str(i), b)