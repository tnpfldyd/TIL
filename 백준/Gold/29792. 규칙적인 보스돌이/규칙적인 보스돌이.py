import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
D = [int(input()) for _ in range(N)]

B = [tuple(map(int, input().split())) for _ in range(K)]

D.sort(reverse=True)

def get_answer(cur):
    dp = [0] * 901
    for p, q in B:
        t = (p + cur - 1) // cur
        if 900 < t: continue
        for j in range(900, 0, -1):
            if j - t >= 0 and dp[j - t] != 0:
                dp[j] = max(dp[j], dp[j - t] + q)
        dp[t] = max(dp[t], q)
    return max(dp)

answer = 0
for i in range(M):
    answer += get_answer(D[i])
print(answer)