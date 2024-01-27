import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M, K = map(int, input().split())
    houses = list(map(int, input().split()))

    cnt = 0
    total = sum(houses[:M])

    if total < K:
        cnt += 1

    if N != M:
        for i in range(N - 1):
            total -= houses[i]
            next_house = (i + M) % N
            total += houses[next_house]

            if total < K:
                cnt += 1
    
    print(cnt)