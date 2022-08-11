for i in range(3):
    cnt = 0
    temp = 0
    num = input()
    result = []
    for j in num:
        if len(result) == 0:
            result.append(j)
            temp += 1
        elif result[-1] == j:
            result.append(j)
            temp += 1
        elif result[-1] != j:
            result.append(j)
            if temp > cnt:
                cnt = temp
                temp = 1
            else:
                temp = 1
    print(max(cnt, temp))