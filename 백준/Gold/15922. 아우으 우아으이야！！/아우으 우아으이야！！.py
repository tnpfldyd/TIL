import sys
input = sys.stdin.readline
N = int(input())
s, e = map(int, input().split())
answer = 0

for _ in range(N - 1):
    nx, ny = map(int, input().split())
    if e >= nx:
        e = max(e, ny)
    else:
        answer += e - s
        s, e = nx, ny
answer += e - s
print(answer)