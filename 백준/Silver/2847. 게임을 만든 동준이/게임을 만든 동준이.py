import sys
input = sys.stdin.readline

N = int(input())
scores = [int(input()) for _ in range(N)]

total_decrease = 0

for i in range(N - 2, -1, -1):
    if scores[i] >= scores[i + 1]:
        decrease = scores[i] - scores[i + 1] + 1
        total_decrease += decrease
        scores[i] -= decrease

print(total_decrease)