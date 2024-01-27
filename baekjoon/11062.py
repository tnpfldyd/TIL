import sys
input = sys.stdin.readline

def game(left, right, turn):
    if left > right: 
        return 0
    if dp[left][right]:
        return dp[left][right]
    if (turn):
        dp[left][right] = max(cards[left] + game(left + 1, right, not turn), cards[right] + game(left, right - 1, not turn))
    else:
        dp[left][right] = min(game(left + 1, right, not turn), game(left, right - 1, not turn))
    return dp[left][right]

for _ in range(int(input())):
    N = int(input())
    cards = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]
    game(0, N - 1, True)
    print(dp[0][N - 1])