import sys
input = sys.stdin.readline

T = int(input())

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    if x > y:
        x, y = y, x
    parents[y] = x

result = []

for _ in range(T):
    N, M = int(input()), int(input())
    parents = [i for i in range(N + 1)]

    flag = False

    for _ in range(M):
        a, b = map(int, input().split())
        x, y = find(a), find(b)
        if x != y:
            union(x, y)
        else:
            flag = True

    if flag:
        result.append(True)
        continue
    temp = set()
    for i in range(1, N + 1):
        temp.add(find(parents[i]))
    result.append(len(temp) != 1)

[print("graph" if answer else "tree") for answer in result]