import bisect

N = int(input())
N_list = list(map(int, input().strip().split()))
result = []
dp = [0] * N
for idx,i in enumerate(N_list):
    if result:
        if i > result[-1]:
            result.append(i)
            dp[idx] = len(result)-1
        else:
            dp[idx] = bisect.bisect_left(result, i)
            result[dp[idx]] = i
    else:
        result.append(i)
        dp[idx] = len(result)-1
cnt = len(result)-1
answer = []
for idx, cost in zip(reversed(dp), reversed(N_list)):
    if cnt == idx:
        answer.append(cost)
        cnt -= 1
print(len(answer))
print(*answer[::-1])