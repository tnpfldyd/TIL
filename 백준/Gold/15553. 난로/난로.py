import sys
input = sys.stdin.readline
N, K = map(int, input().split())
times = [int(input()) for _ in range(N)]
end_time = times[0] + 1
section = []
count = 1
for i in range(1, N):
    cur = times[i]
    if cur != end_time:
        count += 1
        section.append(cur - end_time)
        end_time = cur + 1
    else:
        end_time += 1
if K < count:
    section.sort()
    for i in range(count - K):
        N += section[i]
print(N)