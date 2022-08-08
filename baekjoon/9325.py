T = int(input())
for i in range(T):
    price = int(input())
    cnt = int(input())
    result = 0
    for j in range(cnt):
        cntt, won = map(int, input().split())
        result += won * cntt
    print(price + result)