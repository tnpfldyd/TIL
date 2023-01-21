import sys
input = sys.stdin.readline
N = int(input())
matrix = [[0] * 26 for _ in range(26)]
for i in range(N):
    a, b = input().rstrip().split(' is ')
    matrix[ord(a)-97][ord(b)-97] = 1
for k in range(26):
    for i in range(26):
        for j in range(26):
            if matrix[i][k] == 1 and matrix[k][j] == 1:
                matrix[i][j] = 1
T = int(input())
for i in range(T):
    a, b = input().rstrip().split(' is ')
    if matrix[ord(a)-97][ord(b)-97] == 1:
        print('T')
    else:
        print('F')