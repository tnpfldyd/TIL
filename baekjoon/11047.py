import sys
input = sys.stdin.readline
N, K = map(int, input().split())
result = []
for i in range(N):
    won = int(input())
    result.append(won)
result.sort(reverse = True)
cnt = 0
while K != 0:
    for i in result:
        if K / i > 1:
            cnt += K // i
            K -= K // i * i
print(cnt)