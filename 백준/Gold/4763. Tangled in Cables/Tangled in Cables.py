import sys
input = sys.stdin.readline

length = float(input())
N = int(input())
name_dic = {}
for i in range(N):
    name = input().strip()
    name_dic[name] = i
parents = [i for i in range(N)]


def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    if x < y:
        x, y = y, x
    parents[x] = y

M = int(input())
edges = []
for _ in range(M):
    a, b, c = input().split()
    c = float(c)
    a, b = name_dic[a], name_dic[b]
    edges.append((c, a, b))
    
edges.sort()
result = cnt = 0
for c, a, b in edges:
    x, y = find(a), find(b)
    if x != y:
        result += c
        cnt += 1
        union(x, y)
    if cnt == N - 1:
        break

print(f'Need {"{:.1f}".format(result)} miles of cable' if result <= length else 'Not enough cable')