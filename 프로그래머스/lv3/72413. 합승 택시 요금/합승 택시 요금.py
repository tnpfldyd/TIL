from pprint import pprint
import sys
INF = sys.maxsize
def solution(n, s, a, b, fares):
    matrix = [[INF] * n for _ in range(n)]
    for x, y, cost in fares:
        matrix[x-1][y-1] = cost
        matrix[y-1][x-1] = cost
    for i in range(n):
        matrix[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    answer = INF
    for k in range(n):
        result = matrix[s-1][k] + matrix[k][a-1] + matrix[k][b-1]
        if answer > result:
            answer = result
    return answer