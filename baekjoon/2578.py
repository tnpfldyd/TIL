# from pprint import pprint
import sys
input = sys.stdin.readline
# sys.stdin = open('2578input.txt', 'r')
matrix = [list(map(int, input().rstrip().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
call = [list(map(int, input().rstrip().split())) for _ in range(5)]
cnt = 0
for i in range(5):
    for j in range(5):
        for x in range(5):
            for y in range(5):
                if call[i][j] == matrix[x][y]:
                    cnt += 1
                    visited[x][y] = 1
                    bingo = 0
                    for nx in range(5):
                        if sum(visited[nx]) == 5:
                            bingo += 1
                        if sum([ny[nx] for ny in visited]) == 5:
                            bingo += 1
                    if visited[0][0] + visited[1][1] + visited[2][2] + visited[3][3] + visited[4][4] == 5:
                        bingo += 1
                    if visited[0][4] + visited[1][3] + visited[2][2] + visited[3][1] + visited[4][0] == 5:
                        bingo += 1
                    if bingo >= 3:
                        print(cnt)
                        sys.exit(0)