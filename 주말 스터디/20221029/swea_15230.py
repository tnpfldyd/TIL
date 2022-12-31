T = int(input())
for i in range(1, T+1):
    text = input()
    temp = []
    cnt = 0
    for j in text:
        j = ord(j)-97
        if j == cnt:
            cnt += 1
            temp.append(j)
        elif j != cnt:
            break
    print(f'#{i} {len(temp)}')