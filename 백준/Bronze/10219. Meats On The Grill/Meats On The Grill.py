import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    matrix = [reversed(list(input().strip())) for _ in range(N)]
    for i in matrix:
        print(''.join(i))