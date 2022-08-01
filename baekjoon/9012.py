T = int(input())
for i in range(T):
    Text = input()
    result = []
    for j in Text:
        if j == '(':
            result.append(j)
        else:
            if result:
                result.pop()
            else:
                print('NO')
                break
    else:
        print('YES' if len(result) == 0 else 'NO')
    