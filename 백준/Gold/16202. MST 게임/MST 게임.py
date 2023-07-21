import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M, K = map(int, input().split())

edges = []
for i in range(1, M + 1):
    a, b = map(int, input().split())
    edges.append((i, a, b))

edges.sort()
temp = set()

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x > y:
        x, y = y, x
    parent[x] = y
answer = []
for k in range(K):
    parent = [i for i in range(N + 1)]
    min_num = INF
    cnt = 0
    result = 0
    for edge in edges:
        cost, a, b = edge
        if cost in temp:
            continue
        if cnt + 1 == N:
            break
        x, y = find(a), find(b)
        if x != y:
            union(x, y)
            cnt += 1
            result += cost
            if min_num > cost:
                min_num = cost
    if cnt + 1 == N:
        answer.append(result)
        temp.add(min_num)
    else:
        answer += [0] * (K - k)
        break

print(*answer)