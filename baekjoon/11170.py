T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    result = 0
    for j in range(x, y+1):
        if '0' in str(j):
            result+= str(j).count('0')
    print(result)