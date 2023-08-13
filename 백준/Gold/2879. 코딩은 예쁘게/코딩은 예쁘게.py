N = int(input())
cur = list(map(int, input().split()))
check = list(map(int, input().split()))

for i in range(N):
    cur[i] -= check[i]

cnt = abs(cur[N - 1])
prev = cur[0]

for i in range(1, N):
    if cur[i] ^ prev < 0:
        cnt += abs(prev)
    elif cur[i] ^ (cur[i] - prev) < 0:
        cnt += abs(cur[i] - prev)
    prev = cur[i]

print(cnt)