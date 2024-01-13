from collections import deque

def solve():
    A, B, C = map(int, input().split())
    result = A + B + C
    if result % 3:
        return 0
    q = deque()
    visited = [[False] * 1501 for _ in range(1501)]
    q.append((A, B))
    visited[A][B] = True
    while q:
        a, b = q.popleft()
        temp = [a, b, result - a - b]
        for i in range(3):
            for j in range(3):
                if temp[i] < temp[j]:
                    x = temp[i] * 2
                    y = temp[j] - temp[i]
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    q.append((x, y))
    return 1 if visited[result // 3][result // 3] else 0

print(solve())