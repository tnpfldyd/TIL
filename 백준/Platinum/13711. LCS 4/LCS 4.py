import bisect, sys
input = sys.stdin.readline

N = int(input())
n1_list = list(map(int, input().strip().split()))
n2_list = list(map(int, input().strip().split()))
dp = [0] * (N)
temp = [0] * (N)
for i in range(N):
    dp[n2_list[i]-1] = i

for i in range(N):
    temp[i] = dp[n1_list[i]-1]

result = []
for num in temp:
    if result:
        if result[-1] < num:
            result.append(num)
        else:
            idx = bisect.bisect_left(result, num)
            result[idx] = num
    else:
        result.append(num)

print(len(result))