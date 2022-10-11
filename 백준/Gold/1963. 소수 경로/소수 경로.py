from collections import deque
import sys, math
input = sys.stdin.readline
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
T = int(input())
for _ in range(T):
    s, e = map(int, input().split())
    start = deque()
    visited = [-1] * 10000
    visited[s] = 0
    start.append(s)
    while start:
        x = start.popleft()
        if x == e:
            print(visited[x])
            break
        for i in range(4):
            for j in range(10):
                nx = ''
                for k in range(4):
                    if i == k:
                        nx += str(j)
                    else:
                        nx += str(x)[k]
                nx = int(nx)
                if nx > 999 and visited[nx] == -1 and is_prime_number(nx):
                    visited[nx] = visited[x] + 1
                    start.append(nx)
    else:
        print('Impossible')