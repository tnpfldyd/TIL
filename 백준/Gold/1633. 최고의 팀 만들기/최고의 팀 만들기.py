import sys
input = sys.stdin.readline

info = []
while True:
    try:
        line = input()
        if not line.strip():
            break
        info.append(list(map(int, line.split())))
    except EOFError:
        break

sz = len(info)
MAX_PLAYERS = 15
dp = [[[0 for _ in range(MAX_PLAYERS + 1)] for _ in range(MAX_PLAYERS + 1)] for _ in range(sz + 1)]

for i in range(sz):
    for white in range(MAX_PLAYERS + 1):
        for black in range(MAX_PLAYERS + 1):

            if white + 1 <= MAX_PLAYERS:
                dp[i+1][white+1][black] = max(dp[i+1][white+1][black], 
                                              dp[i][white][black] + info[i][0])

            if black + 1 <= MAX_PLAYERS:
                dp[i+1][white][black+1] = max(dp[i+1][white][black+1], 
                                              dp[i][white][black] + info[i][1])

            dp[i+1][white][black] = max(dp[i+1][white][black], 
                                        dp[i][white][black])

print(dp[sz][MAX_PLAYERS][MAX_PLAYERS])