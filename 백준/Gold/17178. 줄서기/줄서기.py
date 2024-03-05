from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = []
order = []
for _ in range(N):
    line = input().split()
    for i in line:
        name, number = i.split('-')
        number = int(number)
        order.append((name, number))
        q.append((name, number))

q = deque(q)
order.sort()
stack = []
cur = 0
while q or stack:
    check = order[cur]
    if q and q[0] == check:
        cur += 1
        q.popleft()
    elif stack and stack[-1] == check:
        cur += 1
        stack.pop()
    elif q:
        stack.append(q.popleft())
    else:
        break

print("BAD" if q or stack else "GOOD")