import sys

sys.stdin = open("1288input.txt", "r")


T = int(input())

for i in range(1, T+1) :
    a = int(input())

    b = [0]*10

    result = 0
    while(True) :
        if 0 not in b :
            break
        else :
            result += 1
            c = str(a*result)
            for j in range(len(c)) :
                b[int(c[j])] = 1
    print('#'+str(i), c)