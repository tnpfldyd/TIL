import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    if x < y:
        x, y = y, x
    parents[y] = x

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    edges = []
    for i in range(1, N):
        u, c = map(int, input().split())
        edges.append((u, i, c))
    answer = []
    for i in range(M):
        parents = [j for j in range(N + 1)]
        u, v, c = map(int, input().split())
        edges.append((u, v, c))
        edges.sort(key=lambda x : x[2])
        temp = cnt = 0
        for a, b, c in edges:
            a, b = find(a), find(b)
            if a != b:
                union(a, b)
                temp += c
                cnt += 1
            if cnt == N - 1:
                break
        answer.append(temp)
    result = answer[0]
    for i in range(1, len(answer)):
        result ^= answer[i]
    print(result)