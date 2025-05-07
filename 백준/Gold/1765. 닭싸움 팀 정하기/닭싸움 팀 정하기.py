import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
parent = list(range(n))
rank = [0] * n
enemies = [set() for _ in range(n)]

def find(p):
    while parent[p] != p:
        parent[p] = parent[parent[p]]
        p = parent[p]
    return p

def union(p, q):
    rootP = find(p)
    rootQ = find(q)
    if rootP == rootQ:
        return
    if rank[rootP] < rank[rootQ]:
        parent[rootP] = rootQ
    elif rank[rootP] > rank[rootQ]:
        parent[rootQ] = rootP
    else:
        parent[rootQ] = rootP
        rank[rootP] += 1

for _ in range(m):
    t, p, q = input().split()
    p = int(p) - 1
    q = int(q) - 1
    if t == 'F':
        union(p, q)
    else:
        enemies[p].add(q)
        enemies[q].add(p)

for i in range(n):
    if len(enemies[i]) >= 2:
        lst = list(enemies[i])
        base = lst[0]
        for j in range(1, len(lst)):
            union(base, lst[j])

print(len(set(find(i) for i in range(n))))