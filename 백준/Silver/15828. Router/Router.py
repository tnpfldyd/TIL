import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
buffer = deque()

while True:
    packet = int(input())
    if packet == -1:
        break
    elif packet == 0:
        buffer.popleft()
    elif len(buffer) < N:
        buffer.append(packet)

if buffer:
    print(" ".join(map(str, buffer)))
else:
    print("empty")