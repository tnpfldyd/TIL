import math
def solution(fees, records):
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
    return price