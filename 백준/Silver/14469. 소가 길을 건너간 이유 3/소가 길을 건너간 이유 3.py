import sys
input = sys.stdin.readline

N = int(input())
cows = [tuple(map(int, input().split())) for _ in range(N)]

cows.sort()

current_time = 0
for arrival, inspection in cows:
    if current_time < arrival:
        current_time = arrival
    current_time += inspection

print(current_time)