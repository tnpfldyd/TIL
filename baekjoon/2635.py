T = int(input())
result = [[T] for _ in range(T)]
for i in range(T):
    result[i].append(result[i][0] - i)
    start = 0
    minus = 1
    stack = [result[i][minus]]
    while stack:
        suyeol = stack.pop()
        if suyeol < 0:
            break
        kcats = result[i][start] - result[i][minus]
        if kcats >= 0:
            stack.append(kcats); result[i].append(kcats)
            start += 1; minus += 1
temp = max(map(len, (result)))
max_len = [result[i] for i in range(T) if len(result[i]) == temp]
for i in range(T):
    if len(result[i]) == temp:
        print(temp)
        print(*result[i])
# print(*max_len[0])