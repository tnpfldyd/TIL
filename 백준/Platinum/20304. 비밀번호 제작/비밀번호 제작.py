from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = int(input()), int(input())
m_list = list(map(int, input().strip().split()))
visited = [INF] * (N + 1)
start = deque()
for m in m_list:
    visited[m] = 0
    start.append(m)
answer = 0
while start:
    x = start.popleft()
    next_cost = visited[x] + 1
    for i in range(20): # XOR 연산시 XOR 20은 100만이 넘어가기때문에, N의 범위를 초과함.
        next_node = (1 << i) ^ x

        if next_node <= N and visited[next_node] > next_cost:
            visited[next_node] = next_cost
            start.append(next_node)
            if answer < next_cost:
                answer = next_cost
print(answer)
