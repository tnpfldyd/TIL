result = []
for i in range(9):
    a = int(input())
    result.append(a)
print(max(result))
idx = result.index(max(result))
print(idx+1)