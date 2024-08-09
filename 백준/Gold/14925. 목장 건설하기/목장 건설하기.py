def largest_square_pasture(M, N, matrix):
    dp = [[0] * N for _ in range(M)]
    max_length = 0

    for i in range(M):
        for j in range(N):
            if matrix[i][j]:
                continue
            if i == 0 or j == 0:
                dp[i][j] = 1 
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            
            max_length = max(max_length, dp[i][j])
    
    return max_length

M, N = map(int, input().split())
matrix = []
for _ in range(M):
    matrix.append(list(map(int, input().split())))

result = largest_square_pasture(M, N, matrix)
print(result)
