from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

adj = [[] for _ in range(N + 1)]
deg = [0] * (N + 1)
need = [0] * (N + 1)
cnt = [0] * (N + 1)
time = [-1] * (N + 1)

for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    arr.pop()
    adj[i] = arr
    deg[i] = len(arr)
    need[i] = (deg[i] + 1) // 2

M = int(input())
initial = list(map(int, input().split()))

q = deque()

for x in initial:
    time[x] = 0
    q.append(x)

while q:
    cur = q.popleft()
    t = time[cur]
    for nxt in adj[cur]:
        if time[nxt] != -1:
            continue
        cnt[nxt] += 1
        if cnt[nxt] >= need[nxt]:
            time[nxt] = t + 1
            q.append(nxt)

print(*time[1:])