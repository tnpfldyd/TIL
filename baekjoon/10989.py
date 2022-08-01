import sys
input = sys.stdin.readline
T = int(input())
result = []
for i in range(T):
    number = int(input())
    result.append(number)
result.sort()
print(*result, sep='\n')