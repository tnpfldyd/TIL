import sys
input = sys.stdin.readline

n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
info.sort()

value_psum = [0] * (n + 1)

for i in range(1, n + 1):
    value_psum[i] = value_psum[i - 1] + info[i - 1][1]

B = 1
result = 0
for i in range(1, n + 1):
    A = i
    if (-value_psum[B - 1] + info[B - 1][0]) <= (-value_psum[i - 1] + info[i - 1][0]):
        B = i

    result = max(result, value_psum[A] - info[A - 1][0] - value_psum[B - 1] + info[B - 1][0])

print(result)
