from collections import deque
import sys
input = sys.stdin.readline
def bfs(start):
    dec = deque()
    result = [1]
    dec.append(start)
    visited[start] = True
    while dec:
        x = dec.popleft()
        for i in mat[x]:
            if not visited[i]:
                result.append(i)
                dec.append(i)
                visited[i] = True
    return result
T = int(input())
visited = [False] * (T+1)
mat = [[] for _ in range(T+1)]
prev = []
for i in range(T):
    A = list(map(int, input().rstrip().split()))
    if i == T-1:
        if A[0] != 1:
            print(0)
            sys.exit(0)
        prev = A
    else:
        mat[A[0]].append(A[1])
        mat[A[1]].append(A[0])

rev = [0] * (T+1)
for j in range(len(prev)):
    rev[prev[j]] = j
for k in range(1, len(mat)):
    mat[k].sort(key = lambda x : rev[x])
rere = bfs(1)
print(1 if rere == prev else 0)