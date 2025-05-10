import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

timetable = list(map(int, input().split()))
group_seq = [find(a) for a in timetable]

ans = 0
for i in range(1, N):
    if group_seq[i] != group_seq[i - 1]:
        ans += 1

print(ans)