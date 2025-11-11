import sys
input = sys.stdin.readline

N = int(input().strip())
V = list(map(int, input().split()))

limit_next = 0
ans = 0

for i in range(N-1, -1, -1):
    limit_i = min(V[i], limit_next + 1)
    ans += limit_i
    limit_next = limit_i

print(ans)