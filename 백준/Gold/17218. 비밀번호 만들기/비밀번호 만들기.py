string_a = input()
string_b = input()

len_a = len(string_a)
len_b = len(string_b)

dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

for i in range(len_a):
    for j in range(len_b):
        if string_a[i] == string_b[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1 
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

result = ''
while dp[len_a][len_b] != 0: 
    if dp[len_a][len_b] == dp[len_a - 1][len_b]:
        len_a -= 1 
    elif dp[len_a][len_b] == dp[len_a][len_b - 1]:
        len_b -= 1 
    else:
        result += string_a[len_a - 1]
        len_a -= 1 
        len_b -= 1 

print(result[::-1])