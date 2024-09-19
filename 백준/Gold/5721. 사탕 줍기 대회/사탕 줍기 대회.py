import sys
input = sys.stdin.readline

def max_candy_in_row(row):
    if not row:
        return 0
    if len(row) == 1:
        return row[0]
    
    dp = [0] * len(row)
    dp[0] = row[0]
    dp[1] = max(row[0], row[1])
    
    for i in range(2, len(row)):
        dp[i] = max(dp[i-1], dp[i-2] + row[i])
    
    return dp[-1]

def solve():
    while True:
        M, N = map(int, input().split())
        if M == 0 and N == 0:
            break
        
        candy_field = [list(map(int, input().split())) for _ in range(M)]
        
        max_candy_per_row = [max_candy_in_row(row) for row in candy_field]
        
        print(max_candy_in_row(max_candy_per_row))

if __name__ == "__main__":
    solve()