import bisect, sys
input = sys.stdin.readline
N = int(input())
result, N_list = [], []
for _ in range(N):
    a, b = map(int, input().split())
    N_list.append((a, b))
dp = [0] * N
N_list.sort()
for i in range(N):
    a, b = N_list[i]
    if result:
        if result[-1] < b:
            result.append(b)
            dp[i] = len(result)-1
        else:
            idx = bisect.bisect_left(result, b)
            dp[i] = idx
            result[idx] = b
    else:
        result.append(b)
cnt = len(result)-1

answer = []
for a, b in zip(reversed(dp), reversed(N_list)):
    if a == cnt:
        cnt -= 1
    else:
        answer.append(b[0])

print(len(answer))
for i in reversed(answer):
    print(i)