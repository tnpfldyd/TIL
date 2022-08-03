A = input().split()
MAX_A = []
MIN_A = []
for i in A:
    if '6' in i:
        i = i.replace('6', '5')
        MIN_A.append(int(i))
        if '5' in i:
            i = i.replace('5', '6')
            MAX_A.append(int(i))
    elif '5' in i and '6' not in i:
        MIN_A.append(int(i))
        i = i.replace('5', '6')
        MAX_A.append(int(i))
    else:
        MIN_A.append(int(i))
        MAX_A.append(int(i))
print(sum(MIN_A), sum(MAX_A))