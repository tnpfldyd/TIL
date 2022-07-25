T = int(input())
for i in range(T):
    Text = input()
    result = 0
    cnt = 0
    for j in Text:
        if j == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)