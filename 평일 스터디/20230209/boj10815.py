import sys
input = sys.stdin.readline
T = int(input())
numbers = set(map(int, input().split()))
T2 = int(input())
numbers2 = list(map(int, input().split()))
for i in numbers2:
    if i in numbers:
        print(1, end=' ')
    else:
        print(0, end=' ')