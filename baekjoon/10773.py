T = int(input())
result = []
for i in range(T):
    in_put = int(input())
    result.append(in_put) if in_put != 0 else result.pop()
print(sum(result))