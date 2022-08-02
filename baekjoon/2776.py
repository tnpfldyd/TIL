import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    Text1 = int(input())
    numbers1 = set(map(int, input().split()))
    Text2 = int(input())
    numbers2 = list(map(int, input().split()))
    for j in numbers2:
        if j not in numbers1:
            print(0)
        else:
            print(1)