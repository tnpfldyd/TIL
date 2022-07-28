T = int(input())
result = {}
for i in range(1, T+1):
    a = input()
    if a in result:
        result[a] += 1
    else:
        result[a] = 1
best = sorted(result.items(), key = lambda x : (-x[1], x[0])) # -x[1] 은 벨류값을 내림차순 # x[0] 은 키값을 오름차순
print(best[0][0])