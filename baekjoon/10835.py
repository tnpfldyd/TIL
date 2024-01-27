import sys
sys.setrecursionlimit(10 ** 7)
N = int(input())
left_cards = list(map(int, input().split()))
right_cards = list(map(int, input().split()))

dp = [[-1] * N for _ in range(N)]

def get_result(left, right):
    if left == N or right == N:
        return 0
    if dp[left][right] != -1:
        return dp[left][right]
    dp[left][right] = max(get_result(left + 1, right + 1), get_result(left + 1, right))
    if left_cards[left] > right_cards[right]:
        dp[left][right] = max(dp[left][right], get_result(left, right + 1) + right_cards[right])
    return dp[left][right]

print(get_result(0, 0))