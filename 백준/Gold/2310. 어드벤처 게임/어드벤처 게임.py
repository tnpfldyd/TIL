from collections import deque
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    room_type = [None] * (n + 1)
    room_value = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        data = input().split()
        room_type[i] = data[0]
        room_value[i] = int(data[1])
        for x in data[2:]:
            if x == '0':
                break
            graph[i].append(int(x))

    visited = [-1] * (n + 1)
    q = deque()
    q.append((1, 0))
    visited[1] = 0

    while q:
        cur, money = q.popleft()

        if room_type[cur] == 'L':
            money = max(money, room_value[cur])
        elif room_type[cur] == 'T':
            if money < room_value[cur]:
                continue
            money -= room_value[cur]

        if cur == n:
            print("Yes")
            break

        for nxt in graph[cur]:
            if visited[nxt] < money:
                visited[nxt] = money
                q.append((nxt, money))
    else:
        print("No")