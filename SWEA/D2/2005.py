T = int(input())

for i in range(1, T+1):
    result = []
    n = int(input())
    for x in range(n):
        sml = []
        for j in range(x+1):
            if j == 0 or j == x:
                sml.append(1)
            else:
                sml.append(result[x-1][j] + result[x-1][j-1])
        result.append(sml)

    print('#'+str(i))
    for y in result:
        print(*y)