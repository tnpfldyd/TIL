import sys
from queue import PriorityQueue

input = sys.stdin.readline

def is_matrix_valid():
	for j in range(N):
		column_sum = sum(matrix[i][j] for i in range(N))
		if column_sum != columns[j]:
			return False
	return True

def solution():
	column_info = PriorityQueue()
	for i in range(N):
		column_info.put((-columns[i], i))

	for i in range(N):
		popped_queue = []

		for _ in range(rows[i]):
			count, index = column_info.get()
			matrix[i][index] = 1
			popped_queue.append((count + 1, index))

		for item in popped_queue:
			column_info.put(item)

	if not is_matrix_valid():
		print("-1")
	else:
		print("1")
		for row in matrix:
			print(''.join(map(str, row)))

N = int(input())
rows = list(map(int, input().split()))
columns = list(map(int, input().split()))
matrix = [[0] * N for _ in range(N)]

solution()