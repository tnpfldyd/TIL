import sys
input = sys.stdin.readline

total_value, total_item = map(int, input().split())

dp = [[0] * (total_value + 1) for _ in range(total_item + 1)]

chapters = [list(map(int, input().split())) for _ in range(total_item)]

for i in range(1, total_item + 1):
    weight, value = chapters[i - 1]
    for cur_weight in range(total_value + 1):
        if weight <= cur_weight:
            dp[i][cur_weight] = max(dp[i - 1][cur_weight], dp[i - 1][cur_weight - weight] + value)
        else:
            dp[i][cur_weight] = dp[i - 1][cur_weight]

print(dp[total_item][total_value])