fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# result = [14600, 34400, 5000]
import math
cord_dic = {}
result = {}
price = []
for i in records:
    temp = i.split()
    temp[0] = (int(temp[0][0:2]) * 60) + (int(temp[0][3:5]))
    temp[1] = int(temp[1])
    if temp[2] == 'IN':
        cord_dic[temp[1]] = temp[0]
    else:
        if temp[1] not in result:
            result[temp[1]] = temp[0] - cord_dic[temp[1]]
        else:
            result[temp[1]] += temp[0] - cord_dic[temp[1]]
        del cord_dic[temp[1]]
for k, v in cord_dic.items():
    if k not in result:
        result[k] = 1439 - v
    else:
        result[k] += 1439 - v
result = sorted(result.items(), key = lambda x : x[0])
for k, v in result:
    chd = math.ceil((v - fees[0]) / fees[2])
    if chd > 0:
        chd = fees[1] + (fees[3]*chd)
    else:
        chd = fees[1]
    price.append(chd)
print(price)