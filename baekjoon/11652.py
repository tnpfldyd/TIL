T = int(input())
result = {}
for i in range(1, T+1):
    a = int(input())
    if a in result:
        result[a] += 1
    else:
        result[a] = 1
card = sorted(result.items(), key = lambda x : (-x[1], x[0]))
print(card[0][0])