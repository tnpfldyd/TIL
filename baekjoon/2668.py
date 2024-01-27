import sys
input = sys.stdin.readline

N = int(input())
matrix = [[] for _ in range(N + 1)]
rev_matrix = [[] for _ in range(N + 1)]
same = []
for i in range(1, N + 1):
    node = int(input())
    if i == node:
        same.append(i)
    matrix[i].append(node)
    rev_matrix[node].append(i)

stack = []
visited = [False] * (N + 1)
for s in same:
    visited[s] = True
def dfs(cur):
    visited[cur] = True
    for next_node in matrix[cur]:
        if not visited[next_node]:
            dfs(next_node)
    stack.append(cur)

def rev_dfs(cur):
    visited[cur] = True
    temp.append(cur)
    for next_node in rev_matrix[cur]:
        if not visited[next_node]:
            rev_dfs(next_node)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)

visited = [False] * (N + 1)
idx = 0
while stack:
    temp = []
    cur = stack.pop()
    if not visited[cur]:
        rev_dfs(cur)
        if len(temp) > 1:
            while temp:
                same.append(temp.pop())
print(len(same))
same.sort()
for s in same:
    print(s)