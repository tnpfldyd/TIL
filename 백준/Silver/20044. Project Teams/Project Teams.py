import sys
input = sys.stdin.readline

n = int(input())
skills = list(map(int, input().split()))

skills.sort()

min_sum = float('inf')

for i in range(n):
    team_sum = skills[i] + skills[2*n - 1 - i]
    min_sum = min(min_sum, team_sum)

print(min_sum)