def find_kth_binary_string(n, l, k):
    dp = [[0] * 33 for _ in range(33)]
    result = ""

    for i in range(33):
        dp[i][0] = 1
        dp[i][i] = 1

    for i in range(2, 33):
        for j in range(1, i + 1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    def generate_string(remaining_length, remaining_ones, remaining_order):
        nonlocal result
        if remaining_length == 0:
            return
        if remaining_ones == 0:
            result += '0' * remaining_length
            return

        skip = sum(dp[remaining_length - 1][i] for i in range(remaining_ones + 1))

        if skip >= remaining_order:
            result += '0'
            generate_string(remaining_length - 1, remaining_ones, remaining_order)
        else:
            result += '1'
            generate_string(remaining_length - 1, remaining_ones - 1, remaining_order - skip)

    generate_string(n, l, k)
    return result

N, L, I = map(int, input().split())

print(find_kth_binary_string(N, L, I))