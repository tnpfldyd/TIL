import sys

input = sys.stdin.readline

def find(a):
    if a == p[a]:
        return a
    p[a] = find(p[a])
    return p[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        a, b = b, a
    p[b] = a

N, M, T = map(int, input().split())
p = [i for i in range(N + 1)]
v = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    v.append((cost, (a, b)))
v.sort()
ans = 0
cnt = 0
for i in range(len(v)):
    n1, n2 = v[i][1]
    cost = v[i][0]
    if find(n1) != find(n2):
        union(n1, n2)
        ans += 1 * cost
        ans += cnt * T
        cnt += 1
print(ans)