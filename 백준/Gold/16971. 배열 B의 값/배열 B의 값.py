import sys

input = sys.stdin.readline

def calculate_max_sum():
	max_sum = -float('inf')
	for i in range(1, N - 1):
		max_sum = max(max_sum, total_sum - row_sums[i]//2 + row_sums[0])
		max_sum = max(max_sum, total_sum - row_sums[i]//2 + row_sums[N - 1])
	for i in range(1, M - 1):
		max_sum = max(max_sum, total_sum - col_sums[i]//2 + col_sums[0])
		max_sum = max(max_sum, total_sum - col_sums[i]//2 + col_sums[M - 1])
	return max(total_sum, max_sum)

N, M = map(int, input().split())
row_sums = [0] * N
col_sums = [0] * M
total_sum = 0

for i in range(N):
	row = list(map(int, input().split()))
	for j, value in enumerate(row):
		if i == 0 or i == N - 1 or j == 0 or j == M - 1:
			if (i == 0 and j == 0) or (i == 0 and j == M - 1) or (i == N - 1 and j == 0) or (i == N - 1 and j == M - 1):
				row_sums[i] += value
				col_sums[j] += value
				total_sum += value
			else:
				row_sums[i] += 2 * value
				col_sums[j] += 2 * value
				total_sum += 2 * value
		else:
			row_sums[i] += 4 * value
			col_sums[j] += 4 * value
			total_sum += 4 * value

print(calculate_max_sum())