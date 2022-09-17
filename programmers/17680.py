cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
temp = []
cnt = 0
if cacheSize == 0:
    print(len(cities) * 5)
else:
    for i in cities:
        i = i.upper()
        if i in temp:
            if len(temp) < cacheSize:
                temp.append(i)
                cnt += 1
            else:
                q = temp.index(i)
                temp.pop(q)
                temp.append(i)
                cnt += 1
        else:
            if len(temp) < cacheSize:
                temp.append(i)
                cnt += 5
            else:
                temp.pop(0)
                temp.append(i)
                cnt += 5
    print(cnt)