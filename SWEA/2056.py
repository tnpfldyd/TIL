import sys

sys.stdin = open("2056input.txt", "r")

T = int(input())

for i in range(1, T + 1):
    a = input()
    if int(a[0:4]) <= 0:
        print(-1)
    elif int(a[4:6]) in [1,3,5,7,8,10,12]:
        if int(a[6:8]) > 31:
            print('#'+str(i), -1)
        else:
            print('#'+ str(i), a[0:4] + '/' + a[4:6] + '/' + a[6:8])
    elif int(a[4:6]) in [4,6,9,11]:
        if int(a[6:8]) > 30:
            print('#'+str(i), -1)
        else:
            print('#'+ str(i), a[0:4] + '/' + a[4:6] + '/' + a[6:8])
    elif int(a[4:6]) == 2:
        if int(a[6:8]) > 28:
            print('#'+str(i), -1)
        else:
            print('#'+ str(i), a[0:4] + '/' + a[4:6] + '/' + a[6:8])
    else:
        print('#'+str(i), -1)

