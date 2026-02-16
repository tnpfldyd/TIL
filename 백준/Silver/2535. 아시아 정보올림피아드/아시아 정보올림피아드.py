import sys
input = sys.stdin.readline

n = int(input())
students = []
for _ in range(n):
    country, sid, score = map(int, input().split())
    students.append((country, sid, score))

students.sort(key=lambda x: -x[2])

medal_count = {}
winners = []
for country, sid, score in students:
    if len(winners) == 3:
        break
    if medal_count.get(country, 0) < 2:
        winners.append((country, sid))
        medal_count[country] = medal_count.get(country, 0) + 1

for country, sid in winners:
    print(country, sid)
