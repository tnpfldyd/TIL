import sys

sys.stdin = open("2001input.txt", "r")

T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for j in range(N-M+1):
        for k in range(N-M+1):
            bug = 0
            for q in range(M):
                for p in range(M):
                    bug += matrix[j+q][k+p]
            result.append(bug)
    print(f'#{i}', max(result))