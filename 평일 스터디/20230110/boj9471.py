import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    num, M = map(int, input().split())
    dp = [0, 1, 1]
    cnt = 3
    while True:
        dp.append((dp[-1]+dp[-2]) % M)
        if dp[cnt] == 1 and not dp[cnt-1]:
            cnt -= 1
            break
        cnt += 1
    print(num, cnt)