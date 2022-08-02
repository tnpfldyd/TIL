import sys
input = sys.stdin.readline
T = int(input())
result = [0] * 10001
for i in range(T):
    result[int(input())] += 1
for j in range(10001):
    if result[j] != 0:
        for k in range(result[j]):
            print(j)