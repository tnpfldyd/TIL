dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

start_row, start_col, end_row, end_col = map(int, input().split())
matrix = [[0 for _ in range(end_col - start_col + 1)] for _ in range(end_row - start_row + 1)]
total_cells = (end_col - start_col + 1) * (end_row - start_row + 1)
direction = 1
current_x = 0
current_y = 0
current_value = 1
spiral_length = 1

while total_cells > 0:
    for _ in range(2):
        for _ in range(spiral_length):
            if start_row <= current_x <= end_row and start_col <= current_y <= end_col:
                matrix[current_x - start_row][current_y - start_col] = current_value
                total_cells -= 1
                max_value = current_value
            current_x += dx[direction]
            current_y += dy[direction]
            current_value += 1
        direction = (direction - 1) % 4
    spiral_length += 1

max_len = len(str(max_value))
for row in matrix:
    print(" ".join(str(cell).rjust(max_len) for cell in row))
