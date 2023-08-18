from collections import deque
import sys
input = sys.stdin.readline
N, D, K, C = map(int, input().split())
dish = [int(input()) for _ in range(N)]
q = deque()
types = [0] * (D + 1)
cnt = 0

for i in range(K):
    sushi = dish[i]
    q.append(sushi)
    if not types[sushi]:
        cnt += 1
    types[sushi] += 1

answer = cnt
for i in range(N):
    sushi = q.popleft()
    types[sushi] -= 1
    if not types[sushi]:
        cnt -= 1
    nextSushi = dish[((i + K) % N)]
    q.append(nextSushi)
    if not types[nextSushi]:
        cnt += 1
    types[nextSushi] += 1

    temp = cnt + 1 if not types[C] else cnt
    answer = max(answer, temp)

print(answer)