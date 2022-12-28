import bisect
N = int(input())
N_list = list(map(int, input().strip().split()))
dp = [0] * N
temp = []
for idx, cost in enumerate(N_list):
    if temp:
        if temp[-1] < cost:
            temp.append(cost)
            dp[idx] = len(temp)-1
        else:
            dp[idx] = bisect.bisect_left(temp, cost)
            temp[dp[idx]] = cost
    else:
        temp.append(cost)
result = []
cnt = len(temp)-1
for idx, cost in zip(reversed(dp), reversed(N_list)):
    if idx == cnt:
        cnt -= 1
        result.append(cost)
print(len(result))
print(*result[::-1])