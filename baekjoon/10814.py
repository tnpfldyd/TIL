import sys
input = sys.stdin.readline
T = int(input())
member = []
for i in range(T):
    name = (list(input().split()))
    member.append(name)
member.sort(key=lambda x: int(x[0]))
for i in range(T):
    print(*member[i])