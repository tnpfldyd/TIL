from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
scvs = list(map(int, input().strip().split()))

while len(scvs) < 3:
    scvs += [0]

visited = set()
visited.add((scvs[0], scvs[1], scvs[2]))
start = deque()
start.append((scvs[0], scvs[1], scvs[2], 0))
dx, dy, dz = [9,9,3,3,1,1] , [3,1,9,1,3,9] , [1,3,1,9,9,3]
while start:
    x, y, z, cnt = start.popleft()
    if (x, y, z) == (0, 0, 0):
        print(cnt)
        break
    for i in range(6):
        nx, ny, nz = x - dx[i], y - dy[i], z - dz[i]
        nx = 0 if nx < 0 else nx
        ny = 0 if ny < 0 else ny
        nz = 0 if nz < 0 else nz
        if (nx, ny, nz) not in visited:
            visited.add((nx, ny, nz))
            start.append((nx, ny, nz, cnt + 1))