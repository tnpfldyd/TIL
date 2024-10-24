import sys, bisect
input = sys.stdin.readline

N = int(input())

students = []
for _ in range(N):
    h, k = map(int, input().split())
    students.append([h, k])

students.sort(reverse=True)
group = []

for h, k in students:
    index = bisect.bisect_left(group, k)
    if index == 0 or group[0] == k:
        group.insert(0, 1)
    else:
        group[index - 1] += 1

print(len(group))