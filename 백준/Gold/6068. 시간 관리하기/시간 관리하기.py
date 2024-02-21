N = int(input())

times = [tuple(map(int, input().split())) for _ in range(N)]
times = sorted(times, key = lambda x: (-x[1], -x[0]))

result = times[0][1]
for i in range(N):
    s, e = times[i]
    if e <= result:
        result = e - s
    else:
        result -= s
        
print(result if result >= 0 else -1)