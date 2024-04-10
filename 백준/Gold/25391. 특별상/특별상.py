import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
students = []
for _ in range(n):
    a, b = map(int, input().split())
    students.append([a, b, False])

students.sort(key=lambda x: (-x[1], -x[0]))
answer = 0

for i in range(k):
    students[i][2] = True

students.sort(key=lambda x: -x[0])

for i in range(n):
    if not m:
        break
    if not students[i][2]:
        students[i][2] = True
        m -= 1

for i in range(n):
    if students[i][2]:
        answer += students[i][0]

print(answer)