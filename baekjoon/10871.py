a, b = map(int, input().split())
Na = map(int, input().split())
result = []
for i in Na:
    if i < b:
        result.append(i)
print(*result)