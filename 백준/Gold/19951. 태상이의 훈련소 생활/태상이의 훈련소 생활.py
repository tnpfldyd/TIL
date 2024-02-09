import sys
input = sys.stdin.readline

N, M = map(int, input().split())
current_status = list(map(int, input().split()))
temp = [0] * (N + 1)
for _ in range(M):
    a, b, k = map(int, input().split())
    a -= 1; b -= 1
    temp[a] += k; temp[b + 1] -= k

for i in range(1, N + 1):
    temp[i] += temp[i - 1]
    print(current_status[i - 1] + temp[i - 1], end = ' ')