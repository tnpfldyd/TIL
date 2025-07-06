import sys
input = sys.stdin.readline

n = int(input())
students = []

for _ in range(n):
    line = input().split()
    name = line[0]
    korean = int(line[1])
    english = int(line[2])
    math = int(line[3])
    students.append((name, korean, english, math))

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])