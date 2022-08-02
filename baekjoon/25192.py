T = int(input())
result = set()
cnt = 0
for i in range(T):
    name = input()
    if name == 'ENTER':
        cnt += len(result)
        result = set()
    else:
        result.add(name)
print(len(result)+cnt)