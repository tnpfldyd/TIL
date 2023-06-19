import sys
input = sys.stdin.readline

N = int(input())
towns = []
total = 0
for _ in range(N):
    a, b = map(int, input().split())
    towns.append((a, b))
    total += b
cnt = 0
towns.sort()
for number, person in towns:
    cnt += person
    if cnt >= total / 2:
        print(number)
        break
