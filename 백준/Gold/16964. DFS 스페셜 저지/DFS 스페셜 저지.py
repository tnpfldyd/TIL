import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
M = int(input())
matrix = [[] for _ in range(M+1)]
visit = [False] * (M+1)
for i in range(M-1):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
result = list(map(int, input().split()))
if result[0] != 1:
    print(0)
    sys.exit(0)
temp = [0]*(M+1)
for i in range(len(result)):
    temp[result[i]] = i
for i in range(1, len(matrix)):
    matrix[i].sort(key = lambda x : temp[x])
final = []
def dfs(pp):
    final.append(pp)
    visit[pp] = True
    for i in matrix[pp]:
        if not visit[i]:
            dfs(i)
go = dfs(1)
print(1 if final==result else 0)