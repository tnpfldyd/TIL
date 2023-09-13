import sys
input=sys.stdin.readline

N = int(input())
times = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x : x[1], reverse=True)

time = times[0][1] - times[0][0]

for i in range(1, N):
    s, e = times[i]
    if time >= e:
        time = e - s
    else:
        time -= s

print(time)