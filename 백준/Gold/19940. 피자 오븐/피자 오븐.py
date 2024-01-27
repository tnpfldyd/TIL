from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
dx = [60, 10, -10, 1, -1]
dp = ['99999'] * 61
dp[0] = '00000'
q = deque()

def cmp(a, b):
    x = sum(map(int, a))
    y = sum(map(int, b))
    return x < y if x != y else a < b

q.append(0)

while q:
    cur = q.popleft()
    for i in range(5):
        nxt = cur + dx[i]
        if 0 <= nxt <= 60:
            tmp = list(dp[cur])
            tmp[i] = str(int(tmp[i]) + 1)
            if cmp(tmp, list(dp[nxt])):
                dp[nxt] = ''.join(tmp)
                q.append(nxt)

for _ in range(T):
    ans = [0] * 5
    N = int(input())

    ans[0] += N // 60
    N %= 60
    ans = [a + int(b) for a, b in zip(ans, dp[N])]
    print(*ans)