NMAX = 100010

N = 0
inp = [0] * NMAX
sum_arr = [0] * NMAX
val = 0
ret = 0
dp = [[-1] * 4 for _ in range(NMAX)]

def solve(idx, cnt):
    if dp[idx][cnt] >= 0:
        return dp[idx][cnt]

    if idx > N:
        dp[idx][cnt] = 0
    elif cnt == 3:
        if sum_arr[N] - sum_arr[idx-1] == val:
            dp[idx][cnt] = 1
        else:
            dp[idx][cnt] = 0
    else:
        ret = 0
        for nxt in range(idx, N + 1):
            tmp = sum_arr[nxt] - sum_arr[idx-1]
            if tmp == val:
                ret += solve(nxt + 1, cnt + 1)
        dp[idx][cnt] = ret

    return dp[idx][cnt]

N = int(input())
inp = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    sum_arr[i] = sum_arr[i - 1] + inp[i]

if sum_arr[N] % 4 > 0:
    ret = 0
else:
    if not sum_arr[N]:
        zero = 0
        for i in range(1, N + 1):
            zero += (sum_arr[i] == 0)
        ret = (zero - 1) * (zero - 2) * (zero - 3) // 6
    else:
        val = sum_arr[N] // 4
        dp = [[-1] * 4 for _ in range(NMAX)]
        for i in range(1, N + 1):
            if sum_arr[i] == val:
                ret += solve(i + 1, 1)

print(ret)
