import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    if a < b:
        b, a = a, b
    parents[a] = b

T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    parents = [i for i in range(N + 1)]
    edges = sorted([tuple(map(int, input().split())) for _ in range(M)], key=lambda x : x[2])
    cnt = result = 0
    for a, b, c in edges:
        a, b = find(a), find(b)
        if a != b:
            union(a, b)
            cnt += 1
            result += c
        if cnt == N - 1:
            break
    print(f'Case #{i}: {result} meters')