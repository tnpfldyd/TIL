T = map(int, input().split())
result = {}
for i in range(sum(T)):
    name = input()
    if name in result:
        result[name] += 1
    else:
        result[name] = 1
name_result = []
for k, v in result.items():
    if v > 1:
        name_result.append(k)
sort_name = sorted(name_result)
print(len(sort_name))
for j in sort_name:
    print(j)