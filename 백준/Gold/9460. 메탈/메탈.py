import sys

input = sys.stdin.readline

def is_possible(width):
	count = 1
	min_y, max_y = metals[0][1], metals[0][1]
	
	for i in range(1, N):
		if metals[i][1] < min_y:
			min_y = metals[i][1]
		if metals[i][1] > max_y:
			max_y = metals[i][1]
		
		if 2 * width >= (max_y - min_y):
			continue
		else:
			min_y = max_y = metals[i][1]
			count += 1
	
	return count <= K

T = int(input())

for _ in range(T):
	N, K = map(int, input().split())
	metal_data = list(map(int, input().split()))
	metals = [(metal_data[i], metal_data[i + 1]) for i in range(0, 2 * N, 2)]
	metals.sort()
	
	left, right = 0, 200000001
	while right - left > 0.01:
		mid = (left + right) / 2
		
		if is_possible(mid):
			right = mid
		else:
			left = mid
	
	print(f"{right:.1f}")
