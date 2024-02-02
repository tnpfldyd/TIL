import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x - y, x + y))

arr.sort(key = lambda x : (x[0], -x[1]))

cur = 0
answer = 0

for _, b in arr:
    if b > cur:
        answer += 1
        cur = b

print(answer)