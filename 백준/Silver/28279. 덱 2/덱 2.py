from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
N = int(input())
result = []

for _ in range(N):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        dq.appendleft(cmd[1])
    elif cmd[0] == 2:
        dq.append(cmd[1])
    elif cmd[0] == 3:
        result.append(dq.popleft() if dq else -1)
    elif cmd[0] == 4:
        result.append(dq.pop() if dq else -1)
    elif cmd[0] == 5:
        result.append(len(dq))
    elif cmd[0] == 6:
        result.append(1 if not dq else 0)
    elif cmd[0] == 7:
        result.append(dq[0] if dq else -1)
    elif cmd[0] == 8:
        result.append(dq[-1] if dq else -1)

for r in result:
    print(r)