import sys
input = sys.stdin.readline

n = int(input())
students = input().split()
likes = {name: 0 for name in students}

for _ in range(n):
    for name in input().split():
        likes[name] += 1

for name, count in sorted(likes.items(), key=lambda x: (-x[1], x[0])):
    print(name, count)