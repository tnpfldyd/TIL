import sys
input = sys.stdin.readline
INF = sys.maxsize
sys.setrecursionlimit(10 ** 6)

N = int(input())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
order = input()
P = int(input())
start = 0
for i in range(N):
    if order[i] == 'Y':
        start |= 1 << i
visited = [-1] * (1 << N)

def bit_count(x):
    return bin(x)[2:].count('1')

def bit(cur):
    cnt = bit_count(cur)
    if cnt >= P:
        return 0
    if visited[cur] != -1:
        return visited[cur]
    visited[cur] = INF
    for i in range(N):
        if not (cur & 1 << i):
            continue
        for j in range(N):
            if cur & 1 << j:
                continue
            visited[cur] = min(visited[cur], bit(cur | 1 << j) + matrix[i][j])
    return visited[cur]

answer = bit(start)
print(answer if answer != INF else -1)