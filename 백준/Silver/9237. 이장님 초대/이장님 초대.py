import sys
input = sys.stdin.readline

N = int(input())
trees = list(map(int, input().split()))

trees.sort(reverse=True)

max_day = 0
for i in range(N):
    day = i + 1 + trees[i] + 1
    max_day = max(max_day, day)

print(max_day)