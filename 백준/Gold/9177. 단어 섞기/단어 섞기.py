import sys
input = sys.stdin.readline

def is_interleaved(a, b, c):
    l_len = len(a)
    r_len = len(b)

    if l_len + r_len != len(c):
        return False

    dp = [[False] * (r_len + 1) for _ in range(l_len + 1)]
    dp[0][0] = True

    for i in range(1, l_len + 1):
        dp[i][0] = a[i - 1] == c[i - 1] and dp[i - 1][0]
    
    for j in range(1, r_len + 1):
        dp[0][j] = b[j - 1] == c[j - 1] and dp[0][j - 1]

    for i in range(1, l_len + 1):
        for j in range(1, r_len + 1):
            char_a = a[i - 1]
            char_b = b[j - 1]
            char_c = c[i + j - 1]

            if char_a == char_c and dp[i - 1][j]:
                dp[i][j] = True
            if char_b == char_c and dp[i][j - 1]:
                dp[i][j] = True

    return dp[l_len][r_len]

n = int(input())
for loop in range(1, n + 1):
    a, b, c = input().split()
    result = is_interleaved(a, b, c)
    print(f"Data set {loop}: {'yes' if result else 'no'}")
