import sys
input = sys.stdin.readline

arr = [0] * 21
dp = [[[-1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def solve(o1, o2, cnt):
    if cnt == k + 1:
        return 0

    if dp[o1][o2][cnt] != -1:
        return dp[o1][o2][cnt]

    dp[o1][o2][cnt] = min(
        abs(arr[cnt] - o1) + solve(arr[cnt], o2, cnt + 1),
        abs(arr[cnt] - o2) + solve(o1, arr[cnt], cnt + 1)
    )
    
    return dp[o1][o2][cnt]

N = int(input())
open1, open2 = map(int, input().split())
k = int(input())
for i in range(1, k + 1):
    arr[i] = int(input())

print(solve(open1, open2, 1))
