import sys
input = sys.stdin.readline
T = int(input())
result = {}
for i in range(T*2 - 1):
    names = input()
    if names not in result:
        result[names] = 1
    else:
        del result[names]
print(*result)