import itertools
result = ['l','u','r','d']
result.sort()
print(result)
n = 3; m = 4; x = 2; y = 3; r = 3; c = 1; k = 5
answer = []
for i in itertools.product(result, repeat=k):
    temp = []
    temp.append(x)
    temp.append(y)
    for j in i:
        if j == 'l':
            if 1 <= temp[1] - 1 <= m:
                temp[1] -= 1
            else:
                break
        elif j == 'r':
            if 1 <= temp[1] + 1 <= m:
                temp[1] += 1
            else:
                break
        elif j == 'u':
            if 1 <= temp[0] - 1 <= n:
                temp[0] -= 1
            else:
                break
        else:
            if 1 <= temp[0] + 1 <= n:
                temp[0] += 1
            else:
                break
    else:
        if temp[0] == r and temp[1] == c:
            mm = ''
            for j in i:
                mm += j
            print(mm)
    