user = "mrko"
friends = [ ["donut", "andole"], ["donut", "jun"], ["donut", "mrko"], ["shakevan", "andole"], ["shakevan", "jun"], ["shakevan", "mrko"] ]
visitors = ["bedi", "bedi", "donut", "bedi", "shakevan"]
result = ["andole", "jun", "bedi"]
visited = {}
temp = set()
for i in friends:
    if user in i:
        for k in i:
            temp.add(k)
for arr in friends:
    cnt = 0
    for name in arr:
        if name in temp:
            cnt += 1
    if cnt == 1:
        for name in arr:
            if name not in temp:
                if name not in visited:
                    visited[name] = 10
                else:
                    visited[name] += 10
for name in visitors:
    if name not in temp:
        if name not in visited:
            visited[name] = 1
        else:
            visited[name] += 1
visited = sorted(visited.items(), key=lambda x : (-x[1], x[0]))
result = []
for i in visited:
    if len(result) < 5:
        result.append(i[0])
print(result)