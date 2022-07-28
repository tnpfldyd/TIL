import sys
input = sys.stdin.readline
T = int(input())
result = {}
for i in range(T):
    name, status = input().split()
    if status == 'enter':
        result[name] = 1
    else:
        del result[name]
name_sort = sorted(result, reverse = True)
print(*name_sort, sep='\n')
