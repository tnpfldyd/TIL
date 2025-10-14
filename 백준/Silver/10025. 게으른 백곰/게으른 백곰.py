import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * (1000001)

for _ in range(N):
    g, x = map(int, input().split())
    arr[x] = g

window = 2 * K + 1
current = sum(arr[:window])
ans = current

for i in range(window, 1000001):
    current += arr[i] - arr[i - window]
    if current > ans:
        ans = current

print(ans)