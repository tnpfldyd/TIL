import sys
input = sys.stdin.readline
N = int(input())
members = []
for i in range(N):
    age, name = input().strip().split()
    age = int(age)
    members.append((age, i, name))
members.sort()

for member in members:
    print(member[0], member[2])