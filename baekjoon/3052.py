result = []
for i in range(10):
    a = int(input())
    b = a % 42
    result.append(b)
c = set(result)
print(len(c)) 