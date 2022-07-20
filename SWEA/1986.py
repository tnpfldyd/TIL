from re import L


T = int(input())
for i in range(1, T+1):
    a = int(input())
    result = 0
    for j in range(1 , a+1):
        if j % 2 == 1:
            result += j
        else:
            result -= j
    print('#'+str(i), result)
