T = int(input())
for j in range(1, T+1):
    case = int(input())
    result = [[] for _ in range(case)]
    t = input().split()
    for i in range(len(t)):
        result[i].append(t[i][:-1])
        result[i].append(t[i][-1])
    cnt = 0
    for i in result:
        cnt += int(i[0]) ** int(i[1])
    print(f'#{j} {cnt}')