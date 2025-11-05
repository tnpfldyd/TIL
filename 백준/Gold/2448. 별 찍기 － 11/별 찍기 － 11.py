N = int(input())

canvas = [[' '] * (2 * N) for _ in range(N)]

def draw_triangle(y, x, size):
    if size == 3:
        canvas[y][x] = '*'
        canvas[y + 1][x - 1] = '*'
        canvas[y + 1][x + 1] = '*'
        for i in range(-2, 3):
            canvas[y + 2][x + i] = '*'
        return
    
    half = size // 2
    draw_triangle(y, x, half)
    draw_triangle(y + half, x - half, half)
    draw_triangle(y + half, x + half, half)

draw_triangle(0, N - 1, N)

for row in canvas:
    print(''.join(row))