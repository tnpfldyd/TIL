import sys
input = sys.stdin.readline

visited = [0] * (11)
visited[1] = 1; visited[2] = 2; visited[3] = 4; visited[4] = 7
for i in range(5, 11):
    visited[i] = visited[i-1] + visited[i-2] + visited[i-3]

T = int(input())
for _ in range(T):
    print(visited[int(input())])