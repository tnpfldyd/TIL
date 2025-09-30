import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(input().split())

teachers = []
students = []
empty = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            teachers.append((i, j))
        elif board[i][j] == 'S':
            students.append((i, j))
        elif board[i][j] == 'X':
            empty.append((i, j))

def check_surveillance():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for tr, tc in teachers:
        for dr, dc in directions:
            nr, nc = tr + dr, tc + dc
            while 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == 'O':
                    break
                if board[nr][nc] == 'S':
                    return False
                nr += dr
                nc += dc
    return True

for obstacles in combinations(empty, 3):
    for r, c in obstacles:
        board[r][c] = 'O'
    
    if check_surveillance():
        print("YES")
        exit()
    
    for r, c in obstacles:
        board[r][c] = 'X'

print("NO")