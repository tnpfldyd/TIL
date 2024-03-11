from collections import deque

def bfs(u, v):
    q = deque()
    q.append(u)
    dist = [-1] * 1024
    dist[u] = 0

    while q:
        x = q.popleft()

        if x == v:
            return dist[x]
        
        val = 9
        while val - 1 >= 0 and (x & (1 << val)) == 0:
            val -= 1
        for i in range(val):
            nxt = x ^ (1 << i)
            if dist[nxt] == -1:
                q.append(nxt)
                dist[nxt] = dist[x] + 1

        if x + 1 < 1024 and dist[x + 1] == -1:
            q.append(x + 1)
            dist[x + 1] = dist[x] + 1

        if x - 1 >= 0 and dist[x - 1] == -1:
            q.append(x - 1)
            dist[x - 1] = dist[x] + 1

L = int(input(), 2)
K = int(input(), 2)
print(bfs(L, K))