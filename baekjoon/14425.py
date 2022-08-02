import sys
input = sys.stdin.readline
a, b = list(map(int, input().split()))
result = set()
result2 = []
cnt = 0
for i in range(a):
    result.add(input())
for j in range(b):
    result2.append(input())
for k in result2:
    if k in result:
        cnt += 1
print(cnt)