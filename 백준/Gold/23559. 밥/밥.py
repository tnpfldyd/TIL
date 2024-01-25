import sys
input = sys.stdin.readline

n, x = map(int, input().split())
v = []
answer = 0

for _ in range(n):
    a, b = map(int, input().split())
    v.append((a, b))
    answer += b
    x -= 1000

v.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)

for i in range(n):
    if x >= 4000 and v[i][0] - v[i][1] >= 0:
        x -= 4000
        answer += v[i][0] - v[i][1]

print(answer)