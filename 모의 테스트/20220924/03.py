import itertools
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
result = []
for i in range(10, 41, 10):
    result.append(i)
end = []
for i in itertools.product(result, repeat=len(emoticons)):
    temp = []
    for j in range(len(i)):
        temp.append((emoticons[j] - ((emoticons[j] * i[j])//100)))
    final = []
    for j in users:
        result = 0
        for k in range(len(i)):
            if i[k] >= j[0]:
                result += temp[k]
        final.append(result)
    cnt = 0
    temp_price = 0
    for j in range(len(users)):
        if final[j] >= users[j][1]:
            cnt += 1
        else:
            temp_price += final[j]
    print(i)
    print(final)
    print(cnt, temp_price)
    end.append((cnt, temp_price))
end = sorted(end, key = lambda x : (-x[0], -x[1]))
answer = []
for i in end[0]:
    answer.append(i)
