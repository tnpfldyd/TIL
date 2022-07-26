T = int(input())
a = list(map(int, input().split()))
result = []
b = max(a)
for i in a:
    new_a = i / b * 100
    result.append(new_a)
print(sum(result)/T)