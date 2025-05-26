from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

people = list(range(N))

min_diff = float('inf')

for start_team in combinations(people, N//2):
    start_team = list(start_team)
    link_team = [x for x in people if x not in start_team]

    start_power = 0
    for i in range(N//2):
        for j in range(i + 1, N//2):
            start_power += S[start_team[i]][start_team[j]] + S[start_team[j]][start_team[i]]

    link_power = 0
    for i in range(N//2):
        for j in range(i + 1, N//2):
            link_power += S[link_team[i]][link_team[j]] + S[link_team[j]][link_team[i]]

    diff = abs(start_power - link_power)
    min_diff = min(min_diff, diff)

print(min_diff)