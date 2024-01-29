from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize
V = 52

def alpha_to_index(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('A') - 6

def get_max_flow(start, end):
    total_flow = 0
    parent = [-1] * V
    
    while True:
        parent = [-1] * V
        q = deque()
        
        parent[start] = start
        q.append(start)
        
        while q and parent[end] == -1:
            cur = q.popleft()
            for nxt in range(V):
                if capacity[cur][nxt] - flow[cur][nxt] > 0 and parent[nxt] == -1:
                    q.append(nxt)
                    parent[nxt] = cur
        
        if parent[end] == -1:
            break
        
        amount = INF
        i = end
        while i != start:
            amount = min(capacity[parent[i]][i] - flow[parent[i]][i], amount)
            i = parent[i]
        
        i = end
        while i != start:
            flow[parent[i]][i] += amount
            flow[i][parent[i]] -= amount
            i = parent[i]
        
        total_flow += amount
    
    return total_flow

N = int(input())

flow = [[0] * V for _ in range(V)]
capacity = [[0] * V for _ in range(V)]

for _ in range(N):
    a, b, cost = input().strip().split()
    a = alpha_to_index(a)
    b = alpha_to_index(b)
    cost = int(cost)
    capacity[a][b] += cost
    capacity[b][a] += cost

result = get_max_flow(0, 25)
print(result)