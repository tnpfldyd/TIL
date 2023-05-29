import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    points = []
    for _ in range(M):
        a, b = map(int, input().split())
        points.append((b, a))
    points.sort()
    visited = [False] * (N + 1)
    answer = 0
    for b, a in points:
        for i in range(a, b + 1):
            if not visited[i]:
                visited[i] = True
                answer += 1
                break
    print(answer)