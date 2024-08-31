import sys
import heapq
input = sys.stdin.readline

def find_parent(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent_x = find_parent(x)
    while y != parent[y]:
        temp, y = y, parent[y]
        parent[temp] = parent_x
    parent[y] = parent_x

def solve():
    n, m = map(int, input().split())
    maps = [list(input().strip()) for _ in range(n)]

    pq = []
    for i in range(n):
        for j in range(i, n):
            if maps[i][j] == 'Y':
                heapq.heappush(pq, (i, j))

    if len(pq) < m:
        print(-1)
        return

    trash = []
    global parent
    parent = list(range(n))
    answer = [0] * n

    cnt = 0
    while pq:
        i, j = heapq.heappop(pq)
        if find_parent(i) != find_parent(j):
            union(i, j)
            answer[i] += 1
            answer[j] += 1
            cnt += 1
        else:
            heapq.heappush(trash, (i, j))

    if cnt != n - 1:
        print(-1)
        return

    for _ in range(m - cnt):
        i, j = heapq.heappop(trash)
        answer[i] += 1
        answer[j] += 1

    print(*answer, sep=' ')

if __name__ == "__main__":
    solve()