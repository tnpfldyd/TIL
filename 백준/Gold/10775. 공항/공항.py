import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
parent = [i for i in range(G + 1)]
airports = [int(input()) for _ in range(P)]
cnt = 0

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    parent[x] = y

for airport in airports:
    p = find(airport)
    if p:
        union(p, p - 1)
        cnt += 1
    else:
        break

print(cnt)