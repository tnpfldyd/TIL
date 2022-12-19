def solution(n, info):
    result = [0,0,0,0,0,0,0,0,0,0,0]
    max_cnt = 0
    for i in range(1, 1024):
        temp = [0,0,0,0,0,0,0,0,0,0,0]
        i = bin(i)[2:]
        while len(i) < 10:
            i = '0' + i
        lie = 0
        ape = 0
        for j in range(10):
            if i[j] == '1':
                temp[j] = info[j] + 1
        for j in range(10):
            if temp[j] > info[j]:
                lie += 10 - j
            else:
                if info[j] == 0 and temp[j] == 0:
                    continue
                else:
                    ape += 10 - j
        if sum(temp) < n:
            temp[10] = n - sum(temp)
        elif sum(temp) > n:
            continue
        if (lie - ape) > max_cnt:
            max_cnt = lie-ape
            result = temp
        elif lie - ape == max_cnt:
            for i in reversed(range(11)):
                if temp[i] > result[i]:
                    result = temp
                    break
                elif temp[i] < result[i]:
                    break
    if max_cnt == 0:
        return [-1]
    
    return result