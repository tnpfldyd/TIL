import sys
input = sys.stdin.readline
a, b = list(map(int, input().split()))
result = {}
result2 = {}
for i in range(1,a+1):
    name = input().rstrip()
    result[name] = i
    result[i] = name
for j in range(b):
    names = input().rstrip()
    if names.isdigit():
        print(result[int(names)])
    else:
        print(result[names])